# Imágenes del sitio — placeholders y cómo reemplazarlos

El sitio usa **imágenes dummy** (placeholders SVG con etiqueta) en
`public/assets/img/`. Cada una marca dónde va una foto real y con qué
dimensiones. Al reemplazarlas, el sitio toma la imagen nueva automáticamente
en el siguiente `npm run generar && npm run build`.

## Cómo reemplazar una imagen

1. Consigue la foto (ver el prompt de abajo) y **expórtala a las dimensiones
   indicadas** (o mayores con la misma proporción).
2. Guárdala en `public/assets/img/` **con el mismo nombre base** que el
   placeholder, en `.jpg` o `.webp` (recomendado `.webp`, más ligero).
   Ejemplo: `hero.svg` → guarda `hero.jpg`.
3. Actualiza la extensión en `tools/generar.py` (busca `assets/img/hero.svg`
   y cámbialo por `hero.jpg`), o **pídeme que lo haga**: es un search/replace.
4. Corre `npm run generar && npm run build` y revisa con `npm run preview`.

> Sugerencia: comprime las fotos antes de subirlas (TinyPNG / Squoosh) y
> mantén cada archivo por debajo de ~250 KB para que el sitio cargue rápido.

---

## Tabla de imágenes

| Archivo | Sección | Dimensiones | Orientación |
| --- | --- | --- | --- |
| `hero.jpg` | Hero (portada) | 1600 × 1000 | Horizontal |
| `equipo-1.jpg` · `equipo-2.jpg` · `equipo-3.jpg` | Avatares del equipo (hero) | 240 × 240 | Cuadrada |
| `consulta.jpg` | Banda "Tu primera consulta" | 680 × 780 | Vertical |
| `faq.jpg` | Preguntas frecuentes | 680 × 780 | Vertical |
| `blog-1.jpg` | Blog · artículo de divorcio | 480 × 320 | Horizontal |
| `blog-2.jpg` | Blog · artículo de pensión | 480 × 320 | Horizontal |
| `blog-3.jpg` | Blog · artículo de custodia | 480 × 320 | Horizontal |

---

## Descripciones por imagen (para buscar la más acorde)

- **`hero.jpg`** — Foto de portada. Manos de un abogado/a profesional en un
  escritorio elegante **firmando o revisando documentos legales con una pluma**;
  ambiente serio y de confianza, iluminación cálida, tonos neutros oscuros (se
  le aplica un velo oscuro encima, así que debe funcionar con texto blanco
  sobre el lado izquierdo). Sin rostros en primer plano.
- **`equipo-1/2/3.jpg`** — Retratos tipo *headshot* de abogados del despacho,
  fondo neutro, vestimenta formal, gesto cálido y confiable. Idealmente
  personas latinas/mexicanas y con diversidad (al menos una mujer y un hombre).
  Encuadre de hombros hacia arriba, centrado.
- **`consulta.jpg`** — **Balanza de la justicia dorada sobre un escritorio de
  madera** con libros o documentos legales al lado; luz cálida, enfoque
  profesional. (Va sobre fondo oscuro, con esquinas redondeadas.)
- **`faq.jpg`** — Abogada profesional **revisando un expediente en una tablet**
  o leyendo documentos, en una oficina moderna y luminosa; expresión atenta y
  concentrada.
- **`blog-1.jpg`** (Divorcio) — **Pareja firmando documentos de divorcio** frente
  a un abogado, o dos anillos de boda sobre un documento legal; tono sobrio.
- **`blog-2.jpg`** (Pensión alimenticia) — **Documento legal de pensión junto a
  billetes de peso mexicano** y/o una calculadora; concepto de manutención y
  finanzas familiares.
- **`blog-3.jpg`** (Custodia) — **Madre y padre junto a su hijo/a** (manos o
  familia unida), concepto de custodia compartida y bienestar del menor; cálido
  y esperanzador.

---

## Prompt para pegar en Claude Cowork

> Copia y pega el bloque siguiente. Ajusta el estilo si lo deseas.

```text
Necesito 9 imágenes para el sitio web de un despacho de abogados familiares en
la Ciudad de México ("Abogados Familiares CDMX"). Estética: profesional, cálida
y confiable, paleta que combine con coral/durazno (#E08D7D) y carbón oscuro
(#363B42). Todas deben ser fotografías realistas, con licencia de uso comercial
(o generadas), sin marcas de agua ni texto incrustado, y orientadas a un público
mexicano.

Entrégalas con EXACTAMENTE estos nombres de archivo y dimensiones (recorta a la
proporción indicada; formato .webp o .jpg, < 250 KB c/u):

1. hero.jpg — 1600×1000 (horizontal). Manos de un abogado/a profesional en un
   escritorio elegante firmando o revisando documentos legales con pluma;
   ambiente serio, iluminación cálida, tonos neutros oscuros. El sujeto/acción
   debe quedar hacia el lado derecho o centro (el lado izquierdo lleva texto
   encima). Sin rostros en primer plano.

2. equipo-1.jpg — 240×240 (cuadrada). Retrato headshot de una abogada latina,
   fondo neutro, traje formal, gesto cálido y confiable, encuadre de hombros.

3. equipo-2.jpg — 240×240 (cuadrada). Retrato headshot de un abogado latino,
   fondo neutro, traje formal, gesto profesional y cercano.

4. equipo-3.jpg — 240×240 (cuadrada). Retrato headshot de otra/o abogada/o
   latina/o, fondo neutro, coherente con los otros dos retratos.

5. consulta.jpg — 680×780 (vertical). Balanza de la justicia dorada sobre un
   escritorio de madera, con libros o documentos legales al lado; luz cálida.

6. faq.jpg — 680×780 (vertical). Abogada profesional revisando un expediente en
   una tablet en una oficina moderna y luminosa; expresión atenta.

7. blog-1.jpg — 480×320 (horizontal). Pareja firmando documentos de divorcio
   frente a un abogado, o dos anillos de boda sobre un documento legal; tono
   sobrio.

8. blog-2.jpg — 480×320 (horizontal). Documento legal de pensión alimenticia
   junto a billetes de peso mexicano y/o una calculadora; concepto de
   manutención familiar.

9. blog-3.jpg — 480×320 (horizontal). Madre y padre junto a su hijo/a (familia
   unida), concepto de custodia compartida; cálido y esperanzador.

Devuélveme los 9 archivos listos para descargar, nombrados exactamente como
arriba.
```
