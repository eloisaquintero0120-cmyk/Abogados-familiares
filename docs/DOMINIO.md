# Configurar el dominio propio (`abogadosfamiliaresmx.com`)

El sitio funciona sin dominio propio en `https://usuario.github.io/...`, pero
lo recomendable para el despacho es usar el dominio
**`abogadosfamiliaresmx.com`**. Los `canonical`, el `sitemap.xml` y las
imágenes Open Graph ya asumen ese dominio.

> Si el dominio final fuera **otro**, cámbialo en `tools/generar.py`
> (constante `SITE`) y en `public/CNAME`, vuelve a generar (`npm run generar`)
> y haz `push`.

---

## 1. El archivo `CNAME`

Ya existe [`public/CNAME`](../public/CNAME) con el contenido:

```
abogadosfamiliaresmx.com
```

Vite lo copia a `dist/CNAME` en **cada** build, así que el dominio se conserva
en todos los despliegues. **No lo borres.**

## 2. Registrar el dominio en GitHub

1. En GitHub: **Settings → Pages → Custom domain**.
2. Escribe `abogadosfamiliaresmx.com` y pulsa **Save**.
3. GitHub empezará a verificar el DNS (paso siguiente).

## 3. Configurar el DNS (en el proveedor del dominio)

Hay que crear estos registros donde administres el DNS (Cloudflare, GoDaddy,
Namecheap, etc.). Se usa el **apex** (dominio sin `www`) como principal y `www`
como alias.

### Apex `abogadosfamiliaresmx.com` — 4 registros `A`

| Tipo | Nombre / Host | Valor             |
| ---- | ------------- | ----------------- |
| A    | `@`           | `185.199.108.153` |
| A    | `@`           | `185.199.109.153` |
| A    | `@`           | `185.199.110.153` |
| A    | `@`           | `185.199.111.153` |

**Opcional pero recomendado** — soporte IPv6, 4 registros `AAAA`:

| Tipo | Nombre / Host | Valor                   |
| ---- | ------------- | ----------------------- |
| AAAA | `@`           | `2606:50c0:8000::153`   |
| AAAA | `@`           | `2606:50c0:8001::153`   |
| AAAA | `@`           | `2606:50c0:8002::153`   |
| AAAA | `@`           | `2606:50c0:8003::153`   |

### Subdominio `www` — 1 registro `CNAME`

| Tipo  | Nombre / Host | Valor                |
| ----- | ------------- | -------------------- |
| CNAME | `www`         | `USUARIO.github.io.` |

> Sustituye `USUARIO` por el usuario u organización dueña del repositorio.
> GitHub redirige automáticamente entre `www` y el apex según el dominio que
> hayas fijado en Settings → Pages.

> **Nota si usas Cloudflare**: pon los registros en modo **DNS only**
> (nube gris, sin proxy) al menos hasta que GitHub emita el certificado; si no,
> el "Enforce HTTPS" de GitHub puede quedarse bloqueado. Luego puedes activar
> el proxy si lo deseas.

## 4. Verificar la propagación

```bash
# Debe devolver las 4 IPs 185.199.108-111.153
dig abogadosfamiliaresmx.com +noall +answer -t A

# El www debe apuntar a usuario.github.io
dig www.abogadosfamiliaresmx.com +noall +answer -t CNAME
```

La propagación DNS puede tardar de minutos a ~24 h.

## 5. Forzar HTTPS

Cuando GitHub confirme el DNS, emitirá un certificado TLS (Let's Encrypt)
automáticamente. Entonces:

1. Vuelve a **Settings → Pages**.
2. Marca **Enforce HTTPS**.

Esta casilla solo aparece tras validarse el dominio y emitirse el certificado
(puede tardar hasta ~24 h desde que el DNS resuelve).

## 6. Comprobación final

- `https://abogadosfamiliaresmx.com` carga con candado (HTTPS válido).
- `http://…` y `https://www.…` redirigen al dominio con HTTPS.
- Settings → Pages muestra "Your site is live at
  https://abogadosfamiliaresmx.com" y **Enforce HTTPS** activado.

## 7. Post-lanzamiento (SEO)

- Enviar `https://abogadosfamiliaresmx.com/sitemap.xml` a **Google Search
  Console** y **Bing Webmaster Tools**.
- Validar con **Rich Results Test** (los datos estructurados `LegalService`
  y `FAQPage`) y **PageSpeed Insights**.
- Confirmar que la ficha de **Google Business** apunte al dominio.
