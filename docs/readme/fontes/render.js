#!/usr/bin/env node
/**
 * Gera as imagens do README a partir dos HTML desta pasta.
 *
 * Uso (precisa do playwright e do ffmpeg):
 *   NODE_PATH=<pasta node_modules com playwright> node docs/readme/fontes/render.js [nome ...]
 *
 * Sem nome, gera tudo. Cada HTML expõe window.render(t). Os que têm window.DURACAO viram GIF,
 * quadro a quadro, sem depender do relógio do navegador. Os outros viram PNG em escala 2.
 * Saída: docs/readme/imagens/
 */
const path = require('path');
const fs = require('fs');
const os = require('os');
const { execFileSync } = require('child_process');
const { chromium } = require('playwright');

const FONTES = __dirname;
const SAIDA = path.join(FONTES, '..', 'imagens');
const FPS = 12;
const ABERTURA_S = 1.5;
const PECAS = {
  capa: { tipo: 'png' },
  dicionario: { tipo: 'png' },
  caminho: { tipo: 'gif', tambemPng: true },
  conversa: { tipo: 'gif' },
  prova: { tipo: 'gif' },
};

async function abrir(browser, nome, escala) {
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 }, deviceScaleFactor: escala });
  await page.goto('file://' + path.join(FONTES, nome + '.html'));
  await page.evaluate(async () => {
    await document.fonts.ready;
    await Promise.all([...document.images].map((i) => i.complete || new Promise((r) => (i.onload = i.onerror = r))));
  });
  const caixa = await page.locator('.palco').boundingBox();
  await page.setViewportSize({ width: Math.ceil(caixa.width), height: Math.ceil(caixa.height) });
  const fontesOk = await page.evaluate(() => document.fonts.check('800 40px Urbanist'));
  if (!fontesOk) throw new Error(`${nome}: a fonte Urbanist não carregou`);
  return { page, clip: { x: 0, y: 0, width: caixa.width, height: caixa.height } };
}

async function png(browser, nome, sufixo = '') {
  const { page, clip } = await abrir(browser, nome, 2);
  await page.evaluate(() => window.render(window.DURACAO || 0));
  const destino = path.join(SAIDA, nome + sufixo + '.png');
  await page.screenshot({ path: destino, clip });
  await page.close();
  return destino;
}

async function gif(browser, nome) {
  const { page, clip } = await abrir(browser, nome, 1);
  const duracao = await page.evaluate(() => window.DURACAO);
  const pasta = fs.mkdtempSync(path.join(os.tmpdir(), 'sia-' + nome + '-'));
  // O primeiro quadro é a tela pronta, segurada por um instante. Quem pede menos movimento
  // vê o GIF parado no primeiro quadro, e ele precisa mostrar o conteúdo inteiro.
  const abertura = Math.round(ABERTURA_S * FPS);
  const total = Math.round((duracao / 1000) * FPS);
  let n = 0;
  const quadro = async (t) => {
    await page.evaluate((x) => window.render(x), t);
    await page.screenshot({ path: path.join(pasta, `q${String(n++).padStart(4, '0')}.png`), clip });
  };
  for (let i = 0; i < abertura; i++) await quadro(duracao);
  for (let i = 0; i < total; i++) await quadro((i * 1000) / FPS);
  await page.close();
  const destino = path.join(SAIDA, nome + '.gif');
  execFileSync('ffmpeg', [
    '-y', '-loglevel', 'error', '-framerate', String(FPS), '-i', path.join(pasta, 'q%04d.png'),
    '-vf', 'split[a][b];[a]palettegen=max_colors=96:stats_mode=full[p];[b][p]paletteuse=dither=none:diff_mode=rectangle',
    '-loop', '0', destino,
  ]);
  fs.rmSync(pasta, { recursive: true, force: true });
  return destino;
}

(async () => {
  fs.mkdirSync(SAIDA, { recursive: true });
  const nomes = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(PECAS);
  const browser = await chromium.launch();
  try {
    for (const nome of nomes) {
      const peca = PECAS[nome];
      if (!peca) throw new Error(`peça desconhecida: ${nome}`);
      const feitos = [];
      if (peca.tipo === 'gif') feitos.push(await gif(browser, nome));
      if (peca.tipo === 'png' || peca.tambemPng) feitos.push(await png(browser, nome));
      for (const f of feitos) console.log(`${path.relative(process.cwd(), f)}  ${(fs.statSync(f).size / 1024).toFixed(0)} KB`);
    }
  } finally {
    await browser.close();
  }
})().catch((e) => {
  console.error(`Erro ao gerar as imagens: ${e.message}`);
  process.exit(1);
});
