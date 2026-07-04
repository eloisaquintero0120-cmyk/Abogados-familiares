# Despliegue en GitHub Pages con GitHub Actions

El sitio se compila con **Vite** y se publica en **GitHub Pages** de forma
**automática en cada `push` a la rama `main`**, mediante el workflow
[`.github/workflows/deploy.yml`](../.github/workflows/deploy.yml).

No hay que subir la carpeta `dist/` al repositorio: la genera el propio
workflow en el servidor de GitHub. `dist/` y `node_modules/` están en
`.gitignore`.

---

## 1. Requisitos del repositorio

- Repositorio en GitHub (público, o privado con GitHub Pages habilitado en tu plan).
- La rama por defecto debe ser **`main`** (o ajusta la rama en `deploy.yml`).
- Debe estar subido todo el proyecto **incluyendo `package-lock.json`**
  (lo necesita `npm ci` para instalar versiones exactas).

## 2. Activar GitHub Pages con origen "GitHub Actions" (solo la primera vez)

1. En GitHub, entra a **Settings → Pages**.
2. En **Build and deployment → Source**, elige **GitHub Actions**
   (NO "Deploy from a branch").
3. Listo. No hay que elegir rama ni carpeta: el artefacto lo sube el workflow.

> Este paso se hace **una sola vez**. A partir de ahí, cada `push` a `main`
> vuelve a compilar y publicar automáticamente.

## 3. Cómo funciona la automatización

Cada vez que haces `push` a `main` (o lo lanzas a mano desde la pestaña
**Actions → Desplegar en GitHub Pages → Run workflow**), el workflow:

1. **`build`**
   - Descarga el código (`actions/checkout`).
   - Instala Node 22 con caché de `npm`.
   - `npm ci` — instala dependencias desde `package-lock.json`.
   - `npm run build` — Vite compila todas las páginas HTML, agrupa y minifica
     CSS/JS con hash de caché, y copia `public/` (assets, `robots.txt`,
     `sitemap.xml`, `CNAME`, `.nojekyll`) a `dist/`.
   - Sube `dist/` como artefacto de Pages.
2. **`deploy`**
   - Publica ese artefacto en GitHub Pages (`actions/deploy-pages`).
   - Al terminar, la URL publicada aparece en el resumen del workflow y en
     **Settings → Pages**.

Tiempo típico: **~1 minuto**. Puedes seguir el progreso en la pestaña
**Actions**.

## 4. Flujo de trabajo para hacer cambios

```bash
# 1. Editar contenido:
#    - a mano en los .html, o
#    - con el generador (recomendado para cambios globales de header/footer):
npm run generar        # = python3 tools/generar.py

# 2. (Opcional) Previsualizar en local:
npm run dev            # servidor de desarrollo con recarga en caliente
npm run build          # compilar a dist/
npm run preview        # servir dist/ como en producción

# 3. Publicar:
git add -A
git commit -m "Actualiza contenido"
git push origin main   # ← esto dispara el despliegue automático
```

## 5. Comandos disponibles

| Comando           | Qué hace                                                        |
| ----------------- | --------------------------------------------------------------- |
| `npm run dev`     | Servidor de desarrollo Vite con HMR (recarga instantánea).      |
| `npm run build`   | Compila el sitio a `dist/`.                                     |
| `npm run preview` | Sirve `dist/` localmente para revisar el resultado del build.   |
| `npm run generar` | Regenera todos los `.html` desde `tools/generar.py`.            |

## 6. Ruta base (`base`)

`vite.config.js` usa `base: '/'` por defecto, que es lo correcto para:

- un **dominio propio** (`abogadosfamiliarescdmx.com`), o
- una **página de usuario/organización** (`usuario.github.io`).

Si en algún momento publicas como **"project page"** sin dominio propio
(la URL sería `https://usuario.github.io/NOMBRE-REPO/`), las rutas absolutas
`/assets/...` fallarían. En ese caso define la base al compilar:

```yaml
# en deploy.yml, paso "Compilar con Vite"
- name: Compilar con Vite
  run: npm run build
  env:
    VITE_BASE: /NOMBRE-REPO/
```

Con un dominio propio (nuestro caso) **no hay que tocar nada**.

## 7. Resolución de problemas

- **El workflow no aparece / no corre**: confirma que `deploy.yml` está en
  `main` bajo `.github/workflows/` y que en Settings → Pages el origen es
  "GitHub Actions".
- **Falla en `npm ci`**: asegúrate de haber subido `package-lock.json` y de
  que esté sincronizado con `package.json` (`npm install` local y commit).
- **404 en CSS/JS o imágenes tras publicar en subcarpeta**: es el caso de
  `base` de la sección 6 — define `VITE_BASE`.
- **El dominio propio no toma / da error de certificado**: ver
  [`DOMINIO.md`](DOMINIO.md).
- **Permisos**: el workflow ya declara `pages: write` e `id-token: write`; no
  hace falta configurar secretos.
