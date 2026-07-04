import { defineConfig } from 'vite'
import { resolve } from 'node:path'
import { readdirSync } from 'node:fs'

// Raíz del proyecto: los .html se autoran/generan aquí (ver tools/generar.py).
const root = import.meta.dirname

// Carpetas que NO contienen páginas del sitio y no deben recorrerse.
const SKIP = new Set([
  'node_modules',
  'dist',
  'public',
  'tools',
  'docs',
  '.git',
  '.github',
  '.claude',
  '.gstack',
])

// Descubre todas las páginas HTML (raíz + blog/) para configurar la MPA.
// Al ser automático, cada .html nuevo que genere tools/generar.py entra al
// build sin tocar esta configuración.
function findHtml(dir = root, base = '') {
  const pages = []
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    const rel = base ? `${base}/${entry.name}` : entry.name
    if (entry.isDirectory()) {
      if (SKIP.has(entry.name)) continue
      pages.push(...findHtml(resolve(dir, entry.name), rel))
    } else if (entry.name.endsWith('.html')) {
      pages.push(rel)
    }
  }
  return pages
}

const input = Object.fromEntries(
  findHtml().map((page) => [
    page.replace(/\.html$/, '').replace(/\//g, '-'),
    resolve(root, page),
  ]),
)

// https://vite.dev/config/
export default defineConfig({
  // Ruta base pública. En dominio propio (apex) o *.github.io es '/'.
  // Para un "project page" (usuario.github.io/repo/) exporta VITE_BASE=/repo/.
  base: process.env.VITE_BASE || '/',
  appType: 'mpa',
  publicDir: 'public',
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: { input },
  },
})
