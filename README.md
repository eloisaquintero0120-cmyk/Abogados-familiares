# Abogados Familiares CDMX — Sitio web

Sitio para el despacho *Abogados Familiares CDMX* (HTML + CSS + JavaScript vanilla, **sin frameworks de UI**), con la nueva imagen de marca rosa/coral salmón. Se empaqueta con **[Vite](https://vite.dev)** (bundle/minify de CSS y JS) y se publica en **GitHub Pages** de forma **automática en cada `push` a `main`** mediante GitHub Actions.

- 🚀 **Despliegue automático:** [`docs/DESPLIEGUE.md`](docs/DESPLIEGUE.md)
- 🌐 **Dominio propio:** [`docs/DOMINIO.md`](docs/DOMINIO.md)

## Requisitos y comandos

Requiere **Node.js ≥ 20**. Instala dependencias con `npm install`.

| Comando           | Qué hace                                                      |
| ----------------- | ------------------------------------------------------------ |
| `npm run dev`     | Servidor de desarrollo con recarga en caliente (HMR).        |
| `npm run build`   | Compila el sitio a `dist/`.                                   |
| `npm run preview` | Sirve `dist/` localmente, igual que en producción.           |
| `npm run generar` | Regenera todos los `.html` desde `tools/generar.py`.         |

## Estructura

```
index.html                  Home (hero, especialidades, costos, testimonios, FAQ, formulario, mapa)
especialidades.html         Índice de las 9 especialidades
divorcio.html … interdiccion.html   9 páginas de especialidad
blog.html + blog/*.html     Listado y 4 artículos del Blog Jurídico
contacto.html               Formulario + datos + mapa
aviso-de-privacidad.html    Borrador legal (LFPDPPP) — requiere revisión de un abogado
terminos-y-condiciones.html Borrador legal — requiere revisión de un abogado
gracias.html / 404.html     Página de gracias del formulario y error 404
css/styles.css              Hoja de estilos única (design tokens en :root) — Vite la agrupa
js/main.js                  JS vanilla (menú, dropdown, carrusel, formulario AJAX) — Vite lo agrupa
public/                     Copiado tal cual a dist/ por Vite (no se procesa):
  ├─ assets/                Logo (variantes), favicon, apple-touch-icon, og-image
  ├─ robots.txt · sitemap.xml   SEO
  ├─ CNAME                  Dominio propio para GitHub Pages (ver docs/DOMINIO.md)
  └─ .nojekyll              Evita el procesado Jekyll en Pages
tools/generar.py            Generador de páginas (autoría): regenera header/footer consistentes
vite.config.js              Config de Vite (MPA: autodescubre todas las páginas)
package.json                Scripts (dev/build/preview/generar) y dependencia de Vite
.github/workflows/deploy.yml   CI/CD: build + publicación en Pages en cada push a main
docs/                       Guías de despliegue y dominio
dist/                       Salida del build (generada; ignorada por git)
```

## Identidad y datos de contacto (verificados del sitio actual)

- Teléfono: **56 2082 9905** (`tel:+525620829905`)
- WhatsApp: `https://wa.me/5215620829905`
- Email: contacto@abogadosfamiliarescdmx.com
- Dirección: Be Grand Downtown Reforma, Ignacio Ramírez s/n, Col. Tabacalera, Cuauhtémoc, CDMX, C.P. 06030
- Horario: Lun–Vie 9:00–19:00 · Sáb 10:00–14:00

## Pendientes antes de publicar (⚠ confirmar con el despacho)

1. **Formspree**: crear el formulario en [formspree.io](https://formspree.io) (plan gratuito, ~50 envíos/mes) y sustituir `TU_ID_FORMSPREE` en `index.html`, `contacto.html` y `tools/generar.py` por el endpoint real. Mientras tanto, el JS muestra un aviso y redirige la conversión a WhatsApp.
2. **Dominio**: confirmar si se reutiliza `abogadosfamiliarescdmx.com` (los canonical/sitemap y `public/CNAME` ya lo asumen). Si cambia, actualizar `SITE` en `tools/generar.py` **y** `public/CNAME`, y regenerar (`npm run generar`). Guía completa de DNS/HTTPS en [`docs/DOMINIO.md`](docs/DOMINIO.md).
3. **Páginas legales**: el Aviso de Privacidad y los Términos son **borradores** que debe validar un abogado del despacho (LFPDPPP).
4. **Redes sociales**: los iconos del footer apuntan a `#`; poner las URLs reales de Facebook/Instagram/TikTok/LinkedIn.
5. **Email**: el sitio actual usa `contacto@` e `info@`; aquí se usó `contacto@` — confirmar el definitivo.

## Despliegue

El despliegue es **automático**: cada `push` a `main` compila con Vite y publica
en GitHub Pages mediante [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

- Puesta en marcha (una sola vez) y detalles del flujo → **[`docs/DESPLIEGUE.md`](docs/DESPLIEGUE.md)**.
- Configurar el dominio propio, DNS y HTTPS → **[`docs/DOMINIO.md`](docs/DOMINIO.md)**.

Resumen: en *Settings → Pages → Source* elige **GitHub Actions** (no "Deploy from a
branch"); a partir de ahí, cada `push origin main` republica el sitio en ~1 min.

## Editar contenido

Opción A (directa): editar los `.html` a mano — header y footer están repetidos en cada página.

Opción B (recomendada para cambios globales): editar `tools/generar.py` y correr `npm run generar`, que regenera todas las páginas con header/footer consistentes (también reescribe `public/robots.txt` y `public/sitemap.xml`). Los assets de marca se generaron con un script a partir del logo (`IMG_4164.PNG`).

En ambos casos, previsualiza con `npm run dev` (o `npm run build && npm run preview`) y publica con `git push origin main`.

## Notas de diseño

- Paleta anclada al salmón del logo `#E08D7D` (`--rosa-marca`), con coral oscuro `#B64A39` (`--rosa-fuerte`) para botones/enlaces. El salmón puro no cumple contraste AA sobre blanco, y el `#C75C4B` propuesto originalmente tampoco (4.15:1), así que se oscureció hasta 5.21:1 (WCAG 2.1 SC 1.4.3 exige ≥4.5:1 en texto normal).
- Tipografías: Playfair Display (títulos) + Montserrat (cuerpo), Google Fonts subset latin.
- FAQ con `<details>/<summary>` nativos (cero JS); carrusel y menús en JS vanilla.
- Todos los precios llevan el disclaimer "ilustrativos y aproximados".
