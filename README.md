# Abogados Familiares CDMX — Sitio web

Sitio 100% estático (HTML + CSS + JavaScript vanilla, **sin framework ni build step**) para el despacho *Abogados Familiares CDMX*, con la nueva imagen de marca rosa/coral salmón. Listo para publicarse en **GitHub Pages**.

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
css/styles.css              Hoja de estilos única (design tokens en :root)
js/main.js                  JS vanilla: menú, dropdown, carrusel, formulario AJAX
assets/                     Logo (variantes), favicon, apple-touch-icon, og-image
robots.txt / sitemap.xml    SEO
tools/generar.py            Generador opcional de páginas (autoría); NO es un build step:
                            los .html publicados ya están generados y se sirven tal cual
```

## Identidad y datos de contacto (verificados del sitio actual)

- Teléfono: **56 2082 9905** (`tel:+525620829905`)
- WhatsApp: `https://wa.me/5215620829905`
- Email: contacto@abogadosfamiliarescdmx.com
- Dirección: Be Grand Downtown Reforma, Ignacio Ramírez s/n, Col. Tabacalera, Cuauhtémoc, CDMX, C.P. 06030
- Horario: Lun–Vie 9:00–19:00 · Sáb 10:00–14:00

## Pendientes antes de publicar (⚠ confirmar con el despacho)

1. **Formspree**: crear el formulario en [formspree.io](https://formspree.io) (plan gratuito, ~50 envíos/mes) y sustituir `TU_ID_FORMSPREE` en `index.html`, `contacto.html` y `tools/generar.py` por el endpoint real. Mientras tanto, el JS muestra un aviso y redirige la conversión a WhatsApp.
2. **Dominio**: confirmar si se reutiliza `abogadosfamiliarescdmx.com` (los canonical/sitemap ya lo asumen). Si cambia, actualizar `SITE` en `tools/generar.py` y regenerar, o buscar/reemplazar en los .html.
3. **Páginas legales**: el Aviso de Privacidad y los Términos son **borradores** que debe validar un abogado del despacho (LFPDPPP).
4. **Redes sociales**: los iconos del footer apuntan a `#`; poner las URLs reales de Facebook/Instagram/TikTok/LinkedIn.
5. **Email**: el sitio actual usa `contacto@` e `info@`; aquí se usó `contacto@` — confirmar el definitivo.

## Despliegue en GitHub Pages

1. Crear un repositorio **público** (ej. `abogados-familiares-cdmx`) y subir todo a la rama `main` (raíz).
2. *Settings → Pages → Build and deployment → Source: "Deploy from a branch" → Branch `main` / `/ (root)` → Save*. El sitio queda en `https://USUARIO.github.io/abogados-familiares-cdmx/` (las rutas son relativas, funciona en subcarpeta).
3. **Dominio propio** (recomendado): en *Settings → Pages → Custom domain* escribir `abogadosfamiliarescdmx.com` (GitHub crea el archivo `CNAME` en la raíz; debe permanecer ahí en cada despliegue). En el DNS:
   - Apex: 4 registros **A** → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (opcional AAAA: `2606:50c0:8000::153` … `8003::153`).
   - `www`: registro **CNAME** → `USUARIO.github.io`.
   - Verificar con `dig abogadosfamiliarescdmx.com +noall +answer -t A`.
4. Marcar **Enforce HTTPS** (disponible tras la propagación DNS, ~24 h).
5. Post-lanzamiento: enviar `sitemap.xml` a Google Search Console y Bing Webmaster Tools; validar con Rich Results Test y PageSpeed Insights; verificar que Google Business apunte al dominio.

## Editar contenido

Opción A (directa): editar los `.html` a mano — header y footer están repetidos en cada página.

Opción B (recomendada para cambios globales): editar `tools/generar.py` y correr `python3 tools/generar.py`, que regenera todas las páginas con header/footer consistentes. Los assets de marca se generaron con un script a partir del logo (`IMG_4164.PNG`).

## Notas de diseño

- Paleta anclada al salmón del logo `#E08D7D` (`--rosa-marca`), con coral oscuro `#B64A39` (`--rosa-fuerte`) para botones/enlaces. El salmón puro no cumple contraste AA sobre blanco, y el `#C75C4B` propuesto originalmente tampoco (4.15:1), así que se oscureció hasta 5.21:1 (WCAG 2.1 SC 1.4.3 exige ≥4.5:1 en texto normal).
- Tipografías: Playfair Display (títulos) + Montserrat (cuerpo), Google Fonts subset latin.
- FAQ con `<details>/<summary>` nativos (cero JS); carrusel y menús en JS vanilla.
- Todos los precios llevan el disclaimer "ilustrativos y aproximados".
