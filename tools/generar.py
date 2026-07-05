#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador de páginas estáticas de Abogados Familiares CDMX.

Herramienta de autoría OPCIONAL: produce los .html finales que se publican
tal cual en GitHub Pages (no es un build step requerido para el deploy).
Uso:  python3 tools/generar.py
"""
import os
import urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Los .html se generan en la raíz (Vite los toma como entradas de la MPA).
# robots.txt, sitemap.xml y los assets estáticos viven en public/ (Vite los
# copia tal cual a dist/ durante el build).
PUBLICO = os.path.join(RAIZ, 'public')
SITE = 'https://abogadosfamiliaresmx.com'
# --- Contacto ---
WA_NUM = '5215514676633'          # número de WhatsApp (con lada país)
def wa(mensaje):
    """URL de WhatsApp con mensaje pre-cargado."""
    return 'https://wa.me/%s?text=%s' % (WA_NUM, urllib.parse.quote(mensaje))
WA_HOME = wa('Hola, Me gustaría hablar con un especialista en derecho familiar')
WA = WA_HOME                      # mensaje por defecto (home / páginas generales)
TEL_HREF = 'tel:+525514676633'
TEL_TXT = '55 1467 6633'
EMAIL = 'abogadosfamiliarescdmx@gmail.com'
DIRECCION = 'Be Grand Downtown Reforma, Ignacio Ramírez s/n, Col. Tabacalera, Cuauhtémoc, CDMX, C.P. 06030'
FORMSPREE = 'https://formspree.io/f/TU_ID_FORMSPREE'  # ← sustituir por el endpoint real

# --- Redes sociales (URLs reales) ---
REDES_URL = {
    'Facebook':  'https://www.facebook.com/share/1BYgSFy9uL/?mibextid=wwXIfr',
    'Instagram': 'https://www.instagram.com/abogadosfamiliarescdmx?igsh=emxjMWdmbmxqYTQ=',
    'TikTok':    'https://www.tiktok.com/@abogadosfamiliares?_r=1&_t=ZS-97RZH9sUmof',
    'LinkedIn':  'https://www.linkedin.com/in/abogadosfamiliares',
}

# --- Google Maps (ficha del negocio) ---
MAPS_LINK  = 'https://maps.app.goo.gl/17E329L4QLTiiioC8'
MAPS_EMBED = 'https://www.google.com/maps?q=Abogados%20Familiares%20CDMX,%20Ciudad%20de%20M%C3%A9xico&z=16&output=embed'

# ---------------------------------------------------------------- iconos SVG
def icono(nombre, size=28):
    cuerpos = {
        'corazon': '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>',
        'dinero': '<line x1="12" y1="2" x2="12" y2="22"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
        'familia': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
        'escudo': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
        'alerta': '<path d="M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>',
        'documento': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>',
        'pluma': '<path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/>',
        'portafolio': '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
        'persona-ok': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><polyline points="16 11 18 13 22 9"/>',
        'telefono': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
        'correo': '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>',
        'ubicacion': '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
        'reloj': '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    }
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 24 24" '
            'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">%s</svg>') % (size, size, cuerpos[nombre])

WA_SVG = ('<svg xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
          '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>')

REDES = {
    'Facebook': '<path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>',
    'Instagram': '<path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/>',
    'TikTok': '<path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/>',
    'LinkedIn': '<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"/>',
}

# ------------------------------------------------------------- especialidades
ESPECIALIDADES = [
    dict(slug='divorcio', nombre='Divorcio', icono='corazon', precio='Desde $12,500 MXN',
         corta='Divorcio express, incausado y contencioso. Trámite completo desde la demanda hasta la inscripción en el Registro Civil.',
         titulo='Abogados de Divorcio en CDMX',
         meta='Abogados de divorcio en CDMX: express, voluntario, incausado y contencioso. Primera consulta GRATIS. ☎ 55 1467 6633.',
         intro=['Terminar un matrimonio es una de las decisiones más difíciles de la vida. Nuestro equipo te acompaña en todo el proceso para que lo resuelvas de la forma más rápida, económica y pacífica posible, protegiendo tu patrimonio y, sobre todo, a tus hijos.',
                'En la Ciudad de México existe el <strong>divorcio incausado</strong>: no necesitas demostrar ninguna causa ni el consentimiento de tu cónyuge para divorciarte. Basta la voluntad de uno de los dos. Nosotros nos encargamos de la estrategia, la demanda, el convenio y todo el trámite ante el juez de lo familiar.'],
         incluye=['Divorcio express / voluntario (mutuo acuerdo) — el más rápido y económico',
                  'Divorcio incausado (sin necesidad de acuerdo del otro cónyuge)',
                  'Divorcio contencioso con controversias de pensión, custodia o bienes',
                  'Elaboración y negociación del convenio de divorcio',
                  'Liquidación de la sociedad conyugal',
                  'Inscripción de la sentencia en el Registro Civil'],
         faqs=[('¿Cuánto tarda un divorcio en CDMX?', 'Un divorcio voluntario (express) suele resolverse en 1 a 3 meses. Un incausado, en 4 a 8 meses. Un contencioso con controversia de custodia o bienes puede tomar de 6 a 18 meses, según la carga del juzgado.'),
               ('¿Puedo divorciarme si mi pareja no quiere?', 'Sí. En CDMX el divorcio incausado solo requiere la voluntad de uno de los cónyuges. El juez decretará el divorcio aunque la otra parte se oponga; las controversias (custodia, pensión, bienes) se resuelven por separado.'),
               ('¿Qué necesito para iniciar?', 'Acta de matrimonio, actas de nacimiento de los hijos (si los hay), identificación oficial y, de preferencia, información sobre bienes e ingresos. En la primera consulta gratuita revisamos tu caso y te decimos exactamente qué documentos faltan.')]),
    dict(slug='pension-alimenticia', nombre='Pensión Alimenticia', icono='dinero', precio='Desde $22,500 MXN',
         corta='Demanda, cálculo, aumento, reducción y ejecución. Asesoría sobre el RNOA y la nueva ley de pensiones.',
         titulo='Abogados de Pensión Alimenticia en CDMX',
         meta='Demanda, cálculo, aumento y reducción de pensión alimenticia en CDMX. Asesoría sobre el RNOA. Primera consulta GRATIS. ☎ 55 1467 6633.',
         intro=['La pensión alimenticia es un derecho de tus hijos, no un favor. Te ayudamos a demandarla, calcularla correctamente, aumentarla cuando las necesidades crecen, o defenderte de una pensión desproporcionada.',
                'Con la entrada en operación del <strong>Registro Nacional de Obligaciones Alimentarias (RNOA)</strong>, los deudores alimentarios morosos enfrentan consecuencias serias: inscripción en el registro, restricciones para trámites y cargos públicos, e incluso impedimentos migratorios. Conocemos a fondo la nueva legislación y la usamos a favor de tu familia.'],
         incluye=['Demanda inicial de pensión alimenticia y medidas provisionales',
                  'Cálculo de la pensión conforme a ingresos comprobables (y presuntivos)',
                  'Aumento o reducción de pensión por cambio de circunstancias',
                  'Ejecución y cobro de pensiones atrasadas (embargo, descuento de nómina)',
                  'Inscripción de deudores en el RNOA',
                  'Defensa del deudor frente a pensiones desproporcionadas'],
         faqs=[('¿Cómo se calcula la pensión alimenticia?', 'No existe un porcentaje fijo en la ley. El juez pondera las necesidades del acreedor (hijos) y la capacidad económica del deudor. En la práctica, suele fijarse entre el 15% y el 30% de los ingresos por un hijo, más por cada hijo adicional. Si el deudor oculta ingresos, se puede acreditar capacidad económica presuntiva.'),
               ('¿Qué pasa si no pagan la pensión?', 'Procede el embargo de bienes y cuentas, la retención directa del salario, la inscripción en el RNOA y, en casos graves, un proceso penal por incumplimiento de obligaciones alimentarias, con pena de 3 a 5 años de prisión en CDMX.'),
               ('¿Hasta qué edad se paga la pensión?', 'Hasta la mayoría de edad, y se extiende mientras el hijo estudie un grado acorde a su edad (típicamente hasta concluir estudios profesionales) o de forma indefinida si tiene alguna discapacidad.')]),
    dict(slug='guarda-y-custodia', nombre='Guarda y Custodia', icono='familia', precio='Desde $28,000 MXN',
         corta='Custodia exclusiva, compartida y provisional. Régimen de visitas y modificación de custodia.',
         titulo='Abogados de Guarda y Custodia en CDMX',
         meta='Juicios de guarda y custodia en CDMX: exclusiva, compartida, provisional y régimen de visitas. Primera consulta GRATIS. ☎ 55 1467 6633.',
         intro=['Nada importa más que tus hijos. Te representamos en juicios de guarda y custodia con una estrategia centrada en el <strong>interés superior del menor</strong>, que es el criterio que guía todas las decisiones del juez familiar.',
                'Atendemos custodias exclusivas, compartidas y provisionales, así como la fijación o modificación del régimen de visitas y convivencias. También actuamos con urgencia cuando existe riesgo para el menor.'],
         incluye=['Custodia exclusiva o compartida (de común acuerdo o en juicio)',
                  'Custodia provisional y medidas urgentes de protección',
                  'Fijación, ampliación o restricción del régimen de visitas',
                  'Modificación de custodia por cambio de circunstancias',
                  'Convivencias supervisadas',
                  'Restitución de menores'],
         faqs=[('¿A qué edad puede un hijo elegir con quién vivir?', 'No hay una edad fija en la ley. El juez está obligado a escuchar al menor y a valorar su opinión conforme a su edad y madurez (generalmente a partir de los 12 años tiene un peso importante), pero la decisión final siempre se basa en el interés superior del menor.'),
               ('¿La custodia se la dan siempre a la madre?', 'No. La ley no establece preferencia por género; el criterio es el interés superior del menor. En la práctica, los menores de corta edad suelen quedar con la madre salvo que exista riesgo, pero los padres pueden obtener la custodia acreditando mejores condiciones de cuidado.'),
               ('¿Existe la custodia compartida en CDMX?', 'Sí. Aunque el Código Civil de CDMX no la regula como figura autónoma, la SCJN ha avalado que los jueces la otorguen cuando beneficia al menor: requiere acuerdo entre los padres, domicilios cercanos y buena comunicación.')]),
    dict(slug='patria-potestad', nombre='Patria Potestad', icono='escudo', precio='Desde $35,000 MXN',
         corta='Pérdida, suspensión y recuperación. Defensa de tus derechos parentales ante el juez familiar.',
         titulo='Juicios de Patria Potestad en CDMX',
         meta='Pérdida, suspensión y recuperación de la patria potestad en CDMX. Defensa de tus derechos parentales. Primera consulta GRATIS. ☎ 55 1467 6633.',
         intro=['La patria potestad es el conjunto de derechos y obligaciones de los padres sobre sus hijos menores: cuidarlos, educarlos, representarlos legalmente y administrar sus bienes. Perderla —o que el otro progenitor abuse de ella— tiene consecuencias profundas.',
                'Te representamos tanto para <strong>demandar la pérdida o suspensión</strong> de la patria potestad (por violencia, abandono, incumplimiento alimentario reiterado o riesgo para el menor) como para <strong>defenderte</strong> de una demanda injusta y recuperar tus derechos parentales.'],
         incluye=['Demanda de pérdida de patria potestad (abandono, violencia, incumplimiento)',
                  'Suspensión provisional por riesgo al menor',
                  'Defensa frente a demandas de pérdida de patria potestad',
                  'Recuperación / rehabilitación de la patria potestad',
                  'Autorizaciones judiciales (viajes, trámites del menor)',
                  'Representación del menor en conflictos de intereses'],
         faqs=[('¿Por qué causas se pierde la patria potestad?', 'Las principales: violencia familiar contra el menor, abandono de deberes por más de 3 meses, incumplimiento reiterado de la pensión alimenticia, condena penal por delitos dolosos contra el hijo, y poner en riesgo grave la salud o seguridad del menor.'),
               ('¿Perder la patria potestad elimina la obligación de dar pensión?', 'No. La pérdida de la patria potestad no extingue la obligación alimentaria: el progenitor sancionado sigue obligado a pagar pensión, pero pierde derechos de decisión y convivencia.')]),
    dict(slug='violencia-familiar', nombre='Violencia Familiar', icono='alerta', precio='Atención 24/7',
         corta='Órdenes de protección, denuncias y medidas urgentes. Atención inmediata para víctimas.',
         titulo='Abogados en Violencia Familiar — Atención 24/7',
         meta='Atención urgente 24/7 a víctimas de violencia familiar en CDMX: órdenes de protección, denuncias y medidas cautelares. Primera consulta GRATIS. ☎ 55 1467 6633.',
         intro=['Si tú o tus hijos están en peligro, <strong>no estás sola/o</strong>. Actuamos de inmediato para obtener órdenes de protección, presentar denuncias y poner a tu familia a salvo. Atendemos emergencias las 24 horas, los 7 días de la semana.',
                'La violencia familiar no es solo física: también es psicológica, económica, patrimonial y sexual. La ley protege a las víctimas con medidas urgentes que pueden ordenarse en horas, incluyendo la salida del agresor del domicilio y la prohibición de acercarse.',
                '<strong>En emergencia inmediata llama al 911.</strong> Línea Mujeres CDMX: 55 5658 1111.'],
         incluye=['Órdenes de protección de emergencia (24–72 horas)',
                  'Denuncia penal por violencia familiar',
                  'Medidas cautelares: separación del agresor del domicilio, prohibición de acercamiento',
                  'Custodia provisional urgente de los menores',
                  'Acompañamiento ante el Ministerio Público y los Centros de Justicia para las Mujeres',
                  'Juicio de divorcio y reparación del daño derivados de la violencia'],
         faqs=[('¿Qué es una orden de protección?', 'Es una medida urgente que dicta un juez o el Ministerio Público para proteger a la víctima: puede ordenar al agresor salir del domicilio, prohibirle acercarse a ti, a tus hijos, a tu trabajo o escuela, y suspender las convivencias. Puede obtenerse en cuestión de horas.'),
               ('¿Necesito pruebas para denunciar?', 'Tu declaración es el punto de partida y tiene valor probatorio. Ayudan los dictámenes médicos y psicológicos, mensajes, fotografías y testigos, pero la falta de pruebas documentales no impide denunciar ni solicitar medidas de protección.')]),
    dict(slug='testamentos', nombre='Testamentario', icono='documento', precio='Desde $15,000 MXN',
         corta='Elaboración de testamentos, juicios testamentarios e intestamentarios y adjudicación de herencias.',
         titulo='Testamentos y Sucesiones en CDMX',
         meta='Testamentos, juicios sucesorios testamentarios e intestamentarios y adjudicación de herencias en CDMX. Primera consulta GRATIS. ☎ 55 1467 6633.',
         intro=['Proteger el patrimonio de tu familia es un acto de amor. Te asesoramos en la elaboración de testamentos y te representamos en juicios sucesorios para que la herencia llegue a quien corresponde, sin pleitos interminables.',
                'Si tu familiar falleció <strong>sin testamento</strong>, es necesario tramitar un <strong>juicio intestamentario</strong> para declarar herederos y adjudicar los bienes. Si dejó testamento, el <strong>juicio testamentario</strong> lo ejecuta. En ambos casos, el trámite puede ser judicial o, en ciertos supuestos, notarial.'],
         incluye=['Asesoría y elaboración de testamento público abierto',
                  'Juicio sucesorio testamentario (judicial o notarial)',
                  'Juicio intestamentario: declaración de herederos y adjudicación',
                  'Inventarios, avalúos y partición de la herencia',
                  'Cesión de derechos hereditarios',
                  'Controversias entre coherederos e impugnación de testamentos'],
         faqs=[('¿Qué pasa si mi familiar murió sin testamento?', 'Se tramita un juicio intestamentario. La ley llama a heredar, en orden: descendientes, cónyuge, ascendientes, parientes colaterales hasta el cuarto grado y, en su defecto, la concubina o concubinario. El juez (o notario) declara herederos y adjudica los bienes.'),
               ('¿Cuánto tarda una sucesión?', 'Una sucesión sin conflicto entre herederos puede resolverse en 6 a 12 meses (menos si procede la vía notarial). Si hay controversia entre coherederos, puede extenderse considerablemente; por eso conviene buscar acuerdos tempranos.')]),
    dict(slug='contratos-y-convenios', nombre='Contratos y Convenios', icono='pluma', precio='Desde $12,500 MXN',
         corta='Capitulaciones, convenios de divorcio, liquidación de sociedad conyugal y acuerdos de pensión.',
         titulo='Contratos y Convenios Familiares en CDMX',
         meta='Capitulaciones matrimoniales, convenios de divorcio, liquidación de sociedad conyugal y acuerdos de pensión en CDMX. ☎ 55 1467 6633.',
         intro=['Un buen convenio evita un mal juicio. Redactamos y negociamos los acuerdos que dan certeza jurídica a tu familia y a tu patrimonio, y los ratificamos ante el juez para que tengan plena fuerza legal.',
                'Desde las <strong>capitulaciones matrimoniales</strong> antes o durante el matrimonio, hasta el <strong>convenio de divorcio</strong> que regula custodia, pensión, visitas y reparto de bienes: un documento bien hecho hoy te ahorra años de litigio mañana.'],
         incluye=['Capitulaciones matrimoniales (separación de bienes / sociedad conyugal)',
                  'Convenios de divorcio (custodia, pensión, visitas, bienes)',
                  'Liquidación de la sociedad conyugal',
                  'Convenios de pensión alimenticia y su ratificación judicial',
                  'Acuerdos de convivencia y mediación familiar',
                  'Donaciones y acuerdos patrimoniales entre familiares'],
         faqs=[('¿Un convenio privado de pensión tiene validez?', 'Un acuerdo privado obliga a las partes, pero para que sea plenamente ejecutable (por ejemplo, para embargar en caso de incumplimiento) conviene ratificarlo ante el juez de lo familiar o elevarlo a sentencia. Nosotros nos encargamos de ese trámite.'),
               ('¿Puedo cambiar de sociedad conyugal a separación de bienes?', 'Sí. Las capitulaciones matrimoniales pueden otorgarse o modificarse durante el matrimonio mediante un trámite ante notario o juez, liquidando previamente la sociedad conyugal existente.')]),
    dict(slug='gestoria', nombre='Gestoría en Trámites Judiciales y Administrativos', icono='portafolio', precio='Desde $5,500 MXN',
         corta='Corrección de actas, registros extemporáneos, rectificaciones, apostillas e inscripción de sentencias.',
         titulo='Gestoría Familiar y Registro Civil en CDMX',
         meta='Corrección y rectificación de actas, registros extemporáneos, apostillas e inscripción de sentencias en CDMX. ☎ 55 1467 6633.',
         intro=['Un error en un acta puede frenar un trámite de toda la familia: pasaportes, herencias, pensiones, escuelas. Nos encargamos de corregirlo de la vía más rápida posible, administrativa o judicial.',
                'También gestionamos registros extemporáneos de nacimiento, inscripción de sentencias (divorcio, adopción, rectificación) ante el Registro Civil, apostillas y legalizaciones para que tus documentos surtan efectos en México y en el extranjero.'],
         incluye=['Corrección y rectificación de actas (nombres, fechas, datos erróneos)',
                  'Aclaración administrativa ante el Registro Civil',
                  'Juicios de rectificación de acta',
                  'Registro extemporáneo de nacimiento',
                  'Inscripción de sentencias y resoluciones en el Registro Civil',
                  'Apostilla y legalización de documentos'],
         faqs=[('¿La corrección de un acta siempre requiere juicio?', 'No. Los errores ortográficos o mecanográficos evidentes se corrigen por la vía administrativa ante el Registro Civil. Cuando el cambio afecta datos esenciales (filiación, identidad), se requiere un juicio de rectificación. Evaluamos gratis cuál vía aplica a tu caso.')]),
    dict(slug='interdiccion', nombre='Apoyos Extra Ordinarios', icono='persona-ok', precio='Desde $45,000 MXN',
         corta='Declaración de incapacidad legal y designación de tutor y curador.',
         titulo='Juicio de Interdicción en CDMX',
         meta='Juicio de interdicción en CDMX: declaración de estado de incapacidad y designación de tutor y curador para proteger a tu familiar. ☎ 55 1467 6633.',
         intro=['Cuando un familiar no puede gobernarse por sí mismo —por una discapacidad intelectual, un padecimiento psiquiátrico o una enfermedad degenerativa como el Alzheimer— la familia necesita una figura legal para protegerlo a él y a su patrimonio.',
                'El <strong>juicio de interdicción</strong> declara judicialmente el estado de incapacidad y designa un <strong>tutor</strong> (que cuida de la persona y sus bienes) y un <strong>curador</strong> (que vigila al tutor). Te acompañamos en todo el proceso con sensibilidad y experiencia, incluyendo los apoyos extraordinarios que contempla la legislación más reciente.'],
         incluye=['Demanda de interdicción y trámite judicial completo',
                  'Coordinación de los dictámenes médicos requeridos',
                  'Designación de tutor y curador',
                  'Apoyos extraordinarios y salvaguardias (modelo de apoyo a la voluntad)',
                  'Autorizaciones judiciales para actos del tutor (venta de bienes, etc.)',
                  'Rendición de cuentas de la tutela'],
         faqs=[('¿Quién puede promover la interdicción?', 'El cónyuge o concubino, los ascendientes, descendientes o hermanos de la persona, y en ciertos casos el Ministerio Público. El juez resuelve con base en dictámenes médicos y la escucha directa de la persona.'),
               ('¿Cuánto tarda un juicio de interdicción?', 'Típicamente entre 8 y 14 meses, dependiendo de la complejidad médica del caso y de la carga del juzgado. Pueden solicitarse medidas provisionales (tutor interino) desde el inicio.')]),
]

# --- Vista del home: 7 especialidades principales + "otras áreas" al pie ---
ESP_POR_SLUG = {e['slug']: e for e in ESPECIALIDADES}
HOME_ESP_SLUGS = ['pension-alimenticia', 'divorcio', 'contratos-y-convenios',
                  'testamentos', 'interdiccion', 'guarda-y-custodia', 'gestoria']
HOME_ESP = [ESP_POR_SLUG[s] for s in HOME_ESP_SLUGS]
OTRAS_ESP = [e for e in ESPECIALIDADES if e['slug'] not in HOME_ESP_SLUGS]

# Descripciones de marketing para las tarjetas del home (texto del despacho).
HOME_DESC = {
    'pension-alimenticia': 'Garantiza el bienestar de tus hijos. Te asesoramos para asegurar, calcular o modificar el monto justo de los recursos necesarios para el sustento, educación, salud y sano desarrollo de los menores de edad.',
    'divorcio': 'Cierra ciclos de forma legal y tranquila. Llevamos tu proceso de disolución matrimonial (ya sea por mutuo acuerdo o incausado) buscando la vía más rápida, estratégica y menos desgastante para ti y tu familia.',
    'contratos-y-convenios': 'Protege tus acuerdos y tu patrimonio. Redacción, revisión y validación legal de todo tipo de acuerdos familiares, asegurando que cada documento cumpla estrictamente con la legislación de la CDMX para evitar conflictos futuros.',
    'testamentos': 'Asegura el futuro de los tuyos. Te acompañamos en la planeación de tu herencia o en la tramitación del proceso sucesorio (con o sin testamento), garantizando el cumplimiento de la última voluntad y la protección de los bienes familiares.',
    'interdiccion': 'Defensa integral para situaciones especiales. Asistencia legal especializada para personas que requieren medidas de apoyo especiales, salvaguardando sus derechos, autonomía e integridad ante cualquier instancia judicial.',
    'guarda-y-custodia': 'El interés superior de tus hijos es nuestra prioridad. Te ayudamos a determinar quién ejercerá el cuidado directo de los menores y a establecer regímenes de visitas y convivencias sanos, justos y equilibrados.',
    'gestoria': 'Agilizamos tus trámites ante cualquier institución. Nos encargamos del seguimiento, obtención de copias certificadas, búsqueda de expedientes y cualquier gestión administrativa o judicial ante tribunales, fiscalías y dependencias públicas, para que tú no tengas que preocuparte.',
}

# ------------------------------------------------------------------ plantilla
def head(titulo, descripcion, ruta, rel='', extra=''):
    canonical = SITE + '/' + (ruta if ruta != 'index.html' else '')
    return f'''<!DOCTYPE html>
<html lang="es-MX">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<meta name="robots" content="index,follow">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#E08D7D">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_MX">
<meta property="og:site_name" content="Abogados Familiares CDMX">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descripcion}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="MX-CMX">
<meta name="geo.position" content="19.4358;-99.1545">
<meta name="ICBM" content="19.4358, -99.1545">
<link rel="icon" type="image/png" sizes="48x48" href="{rel}assets/favicon-48.png">
<link rel="icon" type="image/png" sizes="512x512" href="{rel}assets/icono-512.png">
<link rel="apple-touch-icon" href="{rel}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}css/styles.css">
{extra}</head>
'''

def navbar(rel='', activo='', wa_link=None):
    wa_link = wa_link or WA
    def cur(p):
        return ' aria-current="page"' if activo == p else ''
    drop = '\n'.join(
        f'          <li><a href="{rel}{e["slug"]}.html">{e["nombre"]}</a></li>'
        for e in ESPECIALIDADES)
    return f'''<header class="header">
  <div class="container navbar">
    <a class="navbar-logo" href="{rel}index.html" aria-label="Abogados Familiares CDMX — Inicio">
      <img src="{rel}assets/logo-color.png" alt="Abogados Familiares CDMX" width="211" height="48">
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="menu-principal" aria-label="Abrir menú">
      <span></span><span></span><span></span>
    </button>
    <ul class="nav-menu" id="menu-principal">
      <li><a href="{rel}index.html"{cur('inicio')}>Inicio</a></li>
      <li class="dropdown">
        <button class="dropdown-toggle" aria-expanded="false" aria-haspopup="true">
          Especialidades
          <svg class="caret" xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"/></svg>
        </button>
        <ul class="dropdown-menu">
          <li><a href="{rel}especialidades.html"><strong>Todas las especialidades</strong></a></li>
{drop}
        </ul>
      </li>
      <li><a href="{rel}blog.html"{cur('blog')}>Blog</a></li>
      <li><a href="{rel}contacto.html"{cur('contacto')}>Contacto</a></li>
      <li class="nav-cta">
        <a class="btn btn-whatsapp" href="{wa_link}" target="_blank" rel="noopener">
          {WA_SVG.format(s=18)} Asesoría GRATIS
        </a>
      </li>
    </ul>
  </div>
</header>
'''

def footer(rel='', wa_link=None):
    wa_link = wa_link or WA
    esp = '\n'.join(f'        <li><a href="{rel}{e["slug"]}.html">{e["nombre"]}</a></li>'
                    for e in ESPECIALIDADES)
    redes = '\n'.join(
        f'        <a href="{REDES_URL.get(nombre, "#")}" target="_blank" rel="noopener" aria-label="{nombre}"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{path}</svg></a>'
        for nombre, path in REDES.items())
    return f'''<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-logo">
        <img src="{rel}assets/logo-blanco.png" alt="Abogados Familiares CDMX" width="227" height="52" loading="lazy">
        <p>Despacho especializado en derecho familiar en CDMX con más de 15 años de experiencia.</p>
        <p>{DIRECCION}<br>A 2 min del Metro Revolución (Línea 2).</p>
        <p><a href="{TEL_HREF}">☎ {TEL_TXT}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div>
        <h4>Especialidades</h4>
        <ul>
{esp}
        </ul>
      </div>
      <div>
        <h4>Recursos</h4>
        <ul>
          <li><a href="{rel}blog.html">Blog Jurídico</a></li>
          <li><a href="{rel}contacto.html">Contacto</a></li>
          <li><a href="{rel}aviso-de-privacidad.html">Aviso de Privacidad</a></li>
          <li><a href="{rel}terminos-y-condiciones.html">Términos y Condiciones</a></li>
        </ul>
        <h4 style="margin-top:1.5rem">Horario</h4>
        <ul>
          <li>Lun–Vie: 9:00–19:00</li>
          <li>Sábado: 10:00–14:00</li>
          <li>Violencia familiar: 24/7</li>
        </ul>
      </div>
      <div>
        <h4>Síguenos</h4>
        <div class="footer-redes">
{redes}
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p style="margin:0">© <span data-anio>2026</span> Abogados Familiares CDMX. Todos los derechos reservados.</p>
      <nav aria-label="Legal">
        <a href="{rel}aviso-de-privacidad.html">Aviso de Privacidad</a>
        <a href="{rel}terminos-y-condiciones.html">Términos y Condiciones</a>
      </nav>
    </div>
  </div>
</footer>
<a class="wa-flotante" href="{wa_link}" target="_blank" rel="noopener" aria-label="Chat por WhatsApp">
  {WA_SVG.format(s=30)}
</a>
<script type="module" src="{rel}js/main.js"></script>
</body>
</html>
'''

def pagina(ruta, titulo, descripcion, cuerpo, activo='', extra_head='', wa_link=None):
    rel = '../' if '/' in ruta else ''
    html = (head(titulo, descripcion, ruta, rel, extra_head)
            + '<body>\n' + navbar(rel, activo, wa_link)
            + '<main id="contenido-principal">\n' + cuerpo + '</main>\n'
            + footer(rel, wa_link))
    destino = os.path.join(RAIZ, ruta)
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, 'w', encoding='utf-8') as f:
        f.write(html)
    print('✓', ruta)

def cta_final(rel='', wa_link=None):
    wa_link = wa_link or WA
    return f'''<section class="seccion cta-final">
  <div class="container">
    <h2>Da el primer paso hoy mismo</h2>
    <p>Tu primera consulta en línea es <strong>GRATIS</strong> y 100% confidencial. Cuéntanos tu caso y te diremos exactamente qué hacer.</p>
    <div class="hero-ctas">
      <a class="btn btn-whatsapp btn-grande" href="{wa_link}" target="_blank" rel="noopener">{WA_SVG.format(s=20)} Consulta GRATIS por WhatsApp</a>
      <a class="btn btn-claro btn-grande" href="{TEL_HREF}">{icono('telefono', 20)} Llamar: {TEL_TXT}</a>
    </div>
  </div>
</section>
'''

# ------------------------------------------------------------------- JSON-LD
JSONLD_LEGAL = '''<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"LegalService",
  "name":"Abogados Familiares CDMX",
  "image":"%s/assets/og-image.png",
  "logo":"%s/assets/icono-512.png",
  "url":"%s/",
  "telephone":"+525514676633",
  "email":"%s",
  "priceRange":"$$",
  "address":{"@type":"PostalAddress","streetAddress":"Be Grand Downtown Reforma, Ignacio Ram\\u00edrez s/n, Col. Tabacalera","addressLocality":"Cuauht\\u00e9moc","addressRegion":"CDMX","postalCode":"06030","addressCountry":"MX"},
  "geo":{"@type":"GeoCoordinates","latitude":19.4358,"longitude":-99.1545},
  "areaServed":{"@type":"City","name":"Ciudad de M\\u00e9xico"},
  "openingHoursSpecification":[
    {"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"19:00"},
    {"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"10:00","closes":"14:00"}
  ]
}
</script>
''' % (SITE, SITE, SITE, EMAIL)

FAQS_HOME = [
    ('¿Cuánto cuesta un divorcio en CDMX en 2026?',
     'El costo depende del tipo de divorcio (voluntario, incausado o contencioso), de si hay hijos y bienes, y del nivel de conflicto. Por eso cada asunto es único y requiere un análisis personalizado: tras tu valoración inicial gratuita evaluamos tu caso y te entregamos una propuesta de honorarios clara y transparente, con opciones de pago accesibles adaptadas a tus necesidades.'),
    ('¿Qué pasa si no pagan la pensión alimenticia?',
     'El incumplimiento tiene consecuencias graves: embargo de bienes y cuentas bancarias, retención directa del salario, inscripción en el RNOA (Registro Nacional de Obligaciones Alimentarias), restricciones para trámites y, en casos graves, proceso penal con pena de 3 a 5 años de prisión en CDMX.'),
    ('¿A qué edad puede un hijo elegir con quién vivir?',
     'No existe una edad fija. El juez debe escuchar al menor y valorar su opinión según su edad y madurez —en la práctica, a partir de los 12 años su opinión pesa mucho—, pero la decisión final siempre se toma conforme al interés superior del menor.'),
    ('¿La primera consulta de verdad es gratis?',
     'Sí. La valoración inicial en línea (o por llamada de hasta 15 minutos) es completamente gratuita y sin compromiso. En ella te decimos si tu caso procede, qué vía conviene y un estimado de costos y tiempos. Confidencialidad absoluta.'),
    ('¿Atienden casos fuera de la Ciudad de México?',
     'Nuestra sede está en CDMX y atendemos toda el área metropolitana, incluido el Estado de México. Las asesorías en línea y por teléfono están disponibles para cualquier parte de la República.'),
    ('¿Ofrecen planes de pago?',
     'Sí. Adaptamos esquemas de pago accesibles a las necesidades de cada cliente. Tras conocer tu caso en la asesoría te entregamos una propuesta de honorarios clara y transparente, con opciones de pago en parcialidades.'),
]

def jsonld_faq(faqs):
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }
    return '<script type="application/ld+json">\n%s\n</script>\n' % json.dumps(data, ensure_ascii=False, indent=1)

# ============================================================== HOME ========
def construir_home():
    tarjetas = '\n'.join(f'''      <article class="tarjeta tarjeta-esp">
        <div class="icono">{icono(e['icono'])}</div>
        <h3>{e['nombre']}</h3>
        <p>{HOME_DESC.get(e['slug'], e['corta'])}</p>
        <a class="enlace" href="{e['slug']}.html">Conocer más →</a>
      </article>''' for e in HOME_ESP)

    otras_html = '\n'.join(
        f'''      <a class="chip-area" href="{e['slug']}.html"><span class="icono">{icono(e['icono'], 20)}</span>{e['nombre']}</a>'''
        for e in OTRAS_ESP)

    faqs_html = '\n'.join(f'''    <details>
      <summary>{q}</summary>
      <div class="faq-respuesta"><p>{a}</p></div>
    </details>''' for q, a in FAQS_HOME)

    testimonios = [
        ('Llegué con mucha preocupación y desde el primer momento me dieron tranquilidad. Siempre atentos, cálidos y muy claros. Se siente cuando trabajan con el corazón. Los recomiendo ampliamente.', 'Cliente verificada · Google'),
        ('Muy buena asesoría, todo explicado con claridad, entendiendo bien los puntos a tratar y mis inquietudes.', 'Cliente verificado · Google'),
        ('Soy del Estado de México, me comuniqué con ellos y me dieron una explicación detallada respecto a mi caso.', 'Josseline · Google'),
        ('Profesionalismo, ética y compromiso con cada caso. Atención clara, cercana y bien informada que genera confianza durante todo el proceso.', 'Cliente verificado · Google'),
    ]
    testimonios_html = '\n'.join(f'''        <figure class="testimonio">
          <div class="estrellas" aria-label="5 de 5 estrellas">★★★★★</div>
          <blockquote>“{t}”</blockquote>
          <figcaption><cite>{c}</cite></figcaption>
        </figure>''' for t, c in testimonios)

    blog_cards = '\n'.join(f'''      <article class="tarjeta tarjeta-blog">
        <div class="portada">{icono(ic, 44)}</div>
        <div class="cuerpo">
          <span class="categoria">{cat}</span>
          <h3><a href="blog/{slug}.html" style="color:inherit">{tit}</a></h3>
          <p>{ext}</p>
          <a class="enlace" href="blog/{slug}.html">Leer más →</a>
        </div>
      </article>''' for slug, cat, tit, ext, ic in [
        ('cuanto-cuesta-divorcio-cdmx-2026', 'Divorcio', '¿Cuánto cuesta un divorcio en CDMX en 2026?',
         'Desglosamos honorarios, gastos judiciales y tiempos por tipo de divorcio, del express al contencioso, y cómo ahorrar.', 'corazon'),
        ('que-pasa-si-no-paga-pension', 'Pensión Alimenticia', '¿Qué pasa si no pagan la pensión alimenticia?',
         'Embargo, retención de salario, RNOA, restricción migratoria y hasta prisión: todas las consecuencias del incumplimiento.', 'dinero'),
        ('custodia-compartida-mexico-2026', 'Custodia', 'Custodia compartida en México 2026',
         'Qué dice la SCJN, qué requisitos piden los jueces y cuándo conviene pedirla. Guía práctica actualizada.', 'familia'),
    ])

    cuerpo = f'''<section class="hero">
  <div class="container hero-grid">
    <div>
      <h1>Abogados familiares en Ciudad de México</h1>
      <p class="subtitulo">Especialistas en divorcio express, pensión alimenticia, guarda y custodia, patria potestad, sucesiones, testamentos, contratos y convenios. Más de 15 años representando familias ante los juzgados familiares de la CDMX. <strong>Primera consulta en línea GRATIS.</strong></p>
      <p class="hero-confianza">
        <span>⭐ 4.9/5 (151 reseñas)</span>
        <span>13,000+ casos resueltos</span>
        <span>15 años de experiencia</span>
        <span>CDMX y área metropolitana</span>
      </p>
      <div class="hero-ctas">
        <a class="btn btn-whatsapp btn-grande" href="{WA}" target="_blank" rel="noopener">{WA_SVG.format(s=20)} Consulta GRATIS por WhatsApp</a>
        <a class="btn btn-secundario btn-grande" href="{TEL_HREF}">{icono('telefono', 20)} Llamar: {TEL_TXT}</a>
      </div>
    </div>
    <div class="hero-visual">
      <img src="assets/logo-color.png" alt="Abogados Familiares CDMX — balanza de la justicia y familia" width="395" height="91" fetchpriority="high">
      <span class="badge">Especialistas exclusivos en Derecho Familiar</span>
    </div>
  </div>
</section>

<section class="stats" aria-label="Cifras del despacho">
  <div class="container stats-grid">
    <div><b>15+</b><span>Años de experiencia</span></div>
    <div><b>13,000+</b><span>Casos resueltos</span></div>
    <div><b>95%</b><span>Casos favorables</span></div>
    <div><b>$0</b><span>Primera consulta</span></div>
    <div><b>24/7</b><span>Urgencias por violencia familiar</span></div>
  </div>
</section>

<section class="seccion" id="especialidades">
  <div class="container">
    <div class="seccion-titulo">
      <span class="kicker">Especialidades</span>
      <h2>¿En qué podemos ayudarte?</h2>
      <p>Atendemos exclusivamente derecho familiar. Cada caso lo lleva un abogado especialista en la materia.</p>
    </div>
    <div class="grid-servicios">
{tarjetas}
    </div>
    <div class="otras-areas">
      <span class="otras-areas-titulo">Otras áreas de práctica</span>
      <div class="chips-areas">
{otras_html}
      </div>
    </div>
  </div>
</section>

<section class="seccion seccion-suave" id="costos">
  <div class="container">
    <div class="seccion-titulo">
      <span class="kicker">Costos de asesoría</span>
      <h2>Elige cómo quieres empezar</h2>
      <p>Tres formas de recibir orientación legal, desde una valoración gratuita hasta una sesión presencial a fondo.</p>
    </div>
    <div class="planes">
      <div class="plan">
        <h3>Valoración inicial online</h3>
        <p class="monto">$0 <small>MXN</small></p>
        <p class="plan-desc">Gratuita. Brindamos asesoría legal en línea sin costo para quienes buscan orientación en materia familiar en CDMX.</p>
        <ul>
          <li>Valoración online gratuita de tu caso</li>
          <li>Te decimos si tu caso procede y qué vía conviene</li>
          <li>Confidencialidad absoluta</li>
        </ul>
        <a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">{WA_SVG.format(s=18)} Empezar gratis</a>
      </div>
      <div class="plan destacado">
        <span class="etiqueta">Más solicitada</span>
        <h3>Asesoría por llamada</h3>
        <p class="monto">$890 <small>MXN</small></p>
        <p class="plan-desc">Duración 40 min. Asesoría personalizada con especialistas en derecho familiar.</p>
        <ul>
          <li>Resolvemos todas tus dudas legales</li>
          <li>Te guiamos paso a paso en tu caso</li>
          <li>Para que tomes decisiones informadas y seguras</li>
        </ul>
        <a class="btn btn-primario" href="contacto.html">Agendar llamada</a>
      </div>
      <div class="plan">
        <h3>Asesoría presencial</h3>
        <p class="monto">$1,890 <small>MXN</small></p>
        <p class="plan-desc">En nuestras oficinas de la CDMX, con cita previa. Atención personalizada y estrategias jurídicas para proteger tus intereses y tu patrimonio.</p>
        <ul>
          <li>Sesión en nuestro despacho (con cita previa)</li>
          <li>Revisión completa de tu expediente</li>
          <li>A 2 minutos del Metro Revolución</li>
        </ul>
        <a class="btn btn-secundario" href="contacto.html">Agendar cita</a>
      </div>
    </div>
  </div>
</section>

<section class="seccion seccion-suave" id="nosotros">
  <div class="container">
    <div class="seccion-titulo">
      <span class="kicker">Quiénes somos</span>
      <h2>Especialistas en Derecho Familiar en Ciudad de México</h2>
    </div>
    <div class="prosa-centro">
      <p>En <strong>Abogados Familiares CDMX</strong> somos un despacho jurídico especializado en derecho familiar con amplia experiencia en la resolución de conflictos legales en la Ciudad de México. Nos enfocamos en brindar asesoría jurídica estratégica y representación legal efectiva para proteger los derechos de nuestros clientes y sus familias.</p>
      <p>Nuestro equipo de abogados familiares en CDMX ha logrado resultados favorables en una amplia variedad de asuntos, incluyendo divorcio incausado, pensión alimenticia, guarda y custodia de menores, régimen de convivencias, adopciones y convenios familiares. Cada caso es atendido con un enfoque profesional, ético y personalizado, buscando siempre soluciones legales que prioricen el bienestar familiar y la seguridad jurídica de nuestros clientes.</p>
    </div>
    <ul class="servicios-lista">
      <li>Asesoría jurídica en derecho familiar en Ciudad de México</li>
      <li>Representación ante Juzgados Familiares en CDMX</li>
      <li>Elaboración de convenios y documentos legales</li>
      <li>Estrategias legales para la resolución de conflictos familiares</li>
      <li>Gestión y acompañamiento en todo el proceso jurídico</li>
    </ul>
    <p class="prosa-centro"><strong>Trabajamos con compromiso, experiencia y resultados comprobados</strong>, brindando soluciones legales claras y efectivas.</p>
  </div>
</section>

<section class="seccion" id="por-que-elegirnos">
  <div class="container dos-columnas">
    <div>
      <span class="kicker" style="display:inline-block;font-size:.8rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--rosa-fuerte);margin-bottom:.5rem">Nuestro compromiso</span>
      <h2>¿Qué puedes esperar de nosotros?</h2>
      <ul class="checklist">
        <li><span class="check">🤝</span><div><b>Compromiso total con tu caso</b><span>Defendemos tus intereses con firmeza en cada etapa del proceso, buscando siempre la mejor solución legal para ti y tu familia.</span></div></li>
        <li><span class="check">📩</span><div><b>Atención clara y oportuna</b><span>Respondemos tus dudas de manera rápida, directa y comprensible, para que siempre tengas certeza sobre el avance de tu asunto.</span></div></li>
        <li><span class="check">🔒</span><div><b>Confidencialidad absoluta</b><span>Toda la información que compartes con nosotros es tratada con estricta reserva y profesionalismo, protegiendo tu privacidad en todo momento.</span></div></li>
        <li><span class="check">💰</span><div><b>Honorarios justos y accesibles</b><span>Ofrecemos costos claros y accesibles, adaptados a las necesidades de cada cliente durante su proceso legal.</span></div></li>
      </ul>
    </div>
    <div class="panel-marca">
      <h3>Garantía de resultados</h3>
      <p>Trabajamos con tres objetivos: <strong>asesoría legal integral</strong>, <strong>resolución eficiente de conflictos</strong> y <strong>proteger el bienestar de tu familia</strong>.</p>
      <p>Si tu caso no procede, te lo decimos desde la primera consulta — gratis y sin compromiso.</p>
      <a class="btn btn-claro" href="{WA}" target="_blank" rel="noopener">{WA_SVG.format(s=18)} Hablar con un abogado</a>
    </div>
  </div>
</section>

<section class="seccion" id="guia-pension">
  <div class="container">
    <div class="seccion-titulo">
      <span class="kicker">Guía legal 2026</span>
      <h2>Pensión Alimenticia en CDMX 2026: guía para proteger los derechos de tus hijos</h2>
    </div>
    <article class="prosa prosa-centro">
      <h3>¿Qué es la pensión alimenticia en Ciudad de México?</h3>
      <p>La pensión alimenticia en la Ciudad de México es un derecho fundamental que garantiza el bienestar económico de los hijos menores de edad y, en determinados casos, del cónyuge o concubino que dependa económicamente de la otra parte. Está regulada por el Código Civil de la CDMX y busca cubrir necesidades esenciales como alimentación, vivienda, educación, atención médica, vestido, transporte y desarrollo integral.</p>
      <h3>¿Cómo solicitar una pensión alimenticia en CDMX?</h3>
      <p>Es recomendable contar con la asesoría de un abogado familiar especializado. El proceso generalmente comprende:</p>
      <ol>
        <li>Presentar una demanda de pensión alimenticia ante el Juzgado Familiar competente.</li>
        <li>Acreditar la relación familiar con actas de nacimiento, matrimonio o documentos correspondientes.</li>
        <li>Demostrar las necesidades económicas del acreedor alimentario.</li>
        <li>Aportar información sobre la capacidad económica de la persona obligada al pago.</li>
      </ol>
      <p>En muchos casos, el juez puede decretar una pensión alimenticia provisional mientras se resuelve el procedimiento definitivo.</p>
      <h3>¿Qué factores considera el juez para fijar el monto?</h3>
      <ul>
        <li>Ingresos y capacidad económica del deudor alimentario.</li>
        <li>Gastos ordinarios y extraordinarios de los hijos.</li>
        <li>Costos de educación, alimentación, salud, vivienda y recreación.</li>
        <li>Número de dependientes económicos.</li>
        <li>Edad y necesidades particulares de los menores.</li>
      </ul>
      <h3>Recomendaciones para fortalecer tu caso</h3>
      <ul class="lista-check">
        <li>Conserva comprobantes de gastos escolares, médicos y de manutención.</li>
        <li>Reúne documentación que acredite ingresos y situación económica.</li>
        <li>Mantén registros bancarios y financieros actualizados.</li>
        <li>Busca asesoría de un abogado de lo familiar en CDMX con experiencia en pensión alimenticia.</li>
      </ul>
      <p>En <strong>Abogados Familiares CDMX</strong> contamos con amplia experiencia en juicios de pensión alimenticia, aumento, reducción, incumplimiento y ejecución de pagos, con representación ante los Juzgados Familiares de la Ciudad de México para proteger los derechos de tus hijos.</p>
    </article>
  </div>
</section>

<section class="seccion seccion-suave" id="novedades">
  <div class="container">
    <div class="seccion-titulo">
      <span class="kicker">Novedades legales</span>
      <h2>Lo más reciente en derecho familiar 2026</h2>
      <p>Actualizaciones que pueden impactar tu caso. Desliza con las flechas.</p>
    </div>
    <div class="carrusel">
      <div class="carrusel-vista">
        <div class="carrusel-pista">
          <article class="novedad">
            <span class="novedad-etiqueta">Pensión Alimenticia</span>
            <h3>Registro Nacional de Deudores Alimentarios 2026: consecuencias de no pagar</h3>
            <p>Durante 2026 se han fortalecido los mecanismos para garantizar el cumplimiento de la pensión mediante el Registro Nacional de Obligaciones Alimentarias, una herramienta que protege los derechos de niñas, niños y adolescentes.</p>
            <p>Quienes incumplen pueden ser inscritos en el Registro Nacional de Deudores Alimentarios, lo que afecta diversos trámites personales, laborales y patrimoniales. En la CDMX, los jueces familiares pueden ordenar descuentos vía nómina, embargos y requerimientos judiciales; el incumplimiento reiterado puede generar consecuencias civiles e incluso penales.</p>
          </article>
          <article class="novedad">
            <span class="novedad-etiqueta">SCJN 2026</span>
            <h3>Pensión alimenticia retroactiva: nuevo criterio de la SCJN</h3>
            <p>La Suprema Corte reforzó el criterio de que el padre biológico puede ser obligado a cubrir pensión alimenticia aun cuando otra persona haya reconocido legalmente al menor.</p>
            <p>También reiteró que el derecho a recibir alimentos es irrenunciable e imprescriptible, por lo que los hijos pueden reclamar pagos adeudados de periodos anteriores.</p>
          </article>
          <article class="novedad">
            <span class="novedad-etiqueta">Divorcio</span>
            <h3>Divorcio incausado en CDMX: qué es y cómo funciona</h3>
            <p>El divorcio incausado permite que cualquiera de los cónyuges solicite la separación sin expresar una causa ni contar con el consentimiento de la otra parte: basta la voluntad de uno de ellos para iniciar el proceso ante un Juzgado Familiar.</p>
            <p>Aunque el matrimonio se disuelve, el juez debe resolver temas importantes como la pensión alimenticia, la guarda y custodia de los hijos, el régimen de convivencias y la división de bienes.</p>
          </article>
        </div>
      </div>
      <div class="carrusel-controles">
        <button type="button" class="carrusel-btn carrusel-prev" aria-label="Novedad anterior">‹</button>
        <div class="carrusel-puntos"></div>
        <button type="button" class="carrusel-btn carrusel-next" aria-label="Novedad siguiente">›</button>
      </div>
    </div>
  </div>
</section>

<section class="seccion" id="mision-vision">
  <div class="container">
    <div class="mv-grid">
      <div class="mv-card">
        <h3>Nuestra Misión</h3>
        <p>Brindar asesoría y representación legal especializada en derecho familiar en la Ciudad de México, con soluciones jurídicas estratégicas, claras y efectivas que protejan los derechos de nuestros clientes y el bienestar de sus familias.</p>
        <p>Atendemos cada caso con profesionalismo, ética y compromiso —en divorcio, pensión alimenticia, guarda y custodia, régimen de convivencias, sucesorios y convenios— buscando siempre una solución justa, ágil y con el menor conflicto posible.</p>
      </div>
      <div class="mv-card">
        <h3>Nuestra Visión</h3>
        <p>Ser un despacho líder en derecho familiar en la Ciudad de México, reconocido por la solidez de nuestras estrategias jurídicas, la eficacia de nuestros resultados y la confianza que generamos en cada cliente.</p>
        <p>Aspiramos a ser la primera opción en CDMX para la resolución de conflictos familiares, con procesos más ágiles y justos, enfocados siempre en el interés superior de niñas, niños y adolescentes y en la estabilidad de las familias.</p>
      </div>
    </div>
  </div>
</section>

<section class="seccion seccion-suave" id="testimonios">
  <div class="container">
    <div class="seccion-titulo">
      <span class="kicker">Testimonios</span>
      <h2>Lo que dicen nuestros clientes</h2>
      <p>Reseñas verificadas en Google · calificación 4.9/5 con 151 reseñas.</p>
    </div>
    <div class="carrusel">
      <div class="carrusel-vista">
        <div class="carrusel-pista">
{testimonios_html}
        </div>
      </div>
      <div class="carrusel-controles">
        <button type="button" class="carrusel-btn carrusel-prev" aria-label="Testimonio anterior">‹</button>
        <div class="carrusel-puntos"></div>
        <button type="button" class="carrusel-btn carrusel-next" aria-label="Testimonio siguiente">›</button>
      </div>
    </div>
  </div>
</section>

<section class="seccion" id="faq">
  <div class="container">
    <div class="seccion-titulo">
      <span class="kicker">Preguntas frecuentes</span>
      <h2>Resolvemos tus dudas</h2>
    </div>
    <div class="faq">
{faqs_html}
    </div>
  </div>
</section>

<section class="seccion seccion-suave" id="blog">
  <div class="container">
    <div class="seccion-titulo">
      <span class="kicker">Blog jurídico</span>
      <h2>Guías legales de derecho familiar</h2>
      <p>Información clara y actualizada para que tomes mejores decisiones.</p>
    </div>
    <div class="grid-blog">
{blog_cards}
    </div>
    <p style="text-align:center;margin-top:2rem"><a class="btn btn-secundario" href="blog.html">Ver todos los artículos</a></p>
  </div>
</section>

<section class="seccion" id="contacto">
  <div class="container">
    <div class="seccion-titulo">
      <span class="kicker">Contacto</span>
      <h2>Recibe asesoría hoy mismo</h2>
      <p>Déjanos tus datos y te contactamos en menos de 2 horas hábiles, o escríbenos directo por WhatsApp.</p>
    </div>
    <div class="form-grid">
      <div class="formulario">
        <form action="{FORMSPREE}" method="POST">
          <label for="f-nombre">Nombre completo</label>
          <input type="text" id="f-nombre" name="nombre" placeholder="Nombre completo" autocomplete="name" required>
          <label for="f-telefono">Teléfono / WhatsApp</label>
          <input type="tel" id="f-telefono" name="telefono" placeholder="Teléfono / WhatsApp" autocomplete="tel" required>
          <label for="f-email">Correo electrónico</label>
          <input type="email" id="f-email" name="email" placeholder="Correo electrónico" autocomplete="email" required>
          <label for="f-tema">¿En qué podemos ayudarte?</label>
          <select id="f-tema" name="tema" required>
            <option value="" disabled selected>Selecciona un tema</option>
            <option>Divorcio</option>
            <option>Pensión alimenticia</option>
            <option>Guarda y custodia</option>
            <option>Patria potestad</option>
            <option>Violencia familiar</option>
            <option>Testamentos y sucesiones</option>
            <option>Otro</option>
          </select>
          <label for="f-mensaje">Mensaje (opcional)</label>
          <textarea id="f-mensaje" name="mensaje" placeholder="Cuéntanos brevemente tu caso (opcional)"></textarea>
          <input type="hidden" name="_subject" value="Nueva consulta desde el sitio web">
          <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
          <p class="consentimiento">Al enviar este formulario aceptas nuestro <a href="aviso-de-privacidad.html">Aviso de Privacidad</a>. Tus datos solo se usan para contactarte sobre tu consulta.</p>
          <button type="submit" class="btn btn-primario btn-grande">Recibir Asesoría</button>
          <p class="form-estado" role="status" aria-live="polite"></p>
        </form>
        <p style="text-align:center;margin:1.25rem 0 0"><a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">{WA_SVG.format(s=18)} Prefiero WhatsApp</a></p>
      </div>
      <div>
        <ul class="contacto-datos">
          <li><span class="icono">{icono('ubicacion', 22)}</span><div><b>Ubicación</b><span>{DIRECCION}.<br>A 2 min del Metro Revolución (Línea 2).</span></div></li>
          <li><span class="icono">{icono('telefono', 22)}</span><div><b>Teléfono</b><a href="{TEL_HREF}">{TEL_TXT}</a></div></li>
          <li><span class="icono">{icono('correo', 22)}</span><div><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
          <li><span class="icono">{icono('reloj', 22)}</span><div><b>Horario</b><span>Lun–Vie 9:00–19:00 · Sáb 10:00–14:00<br>Urgencias por violencia familiar: 24/7</span></div></li>
        </ul>
        <div class="mapa">
          <iframe src="{MAPS_EMBED}" title="Mapa de la ubicación del despacho — Abogados Familiares CDMX, Col. Tabacalera, CDMX" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
          <p style="margin:.6rem 0 0;text-align:center"><a href="{MAPS_LINK}" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
        </div>
      </div>
    </div>
  </div>
</section>
'''
    pagina('index.html',
           'Abogados Familiares CDMX | Divorcio, Pensión y Custodia',
           'Despacho de abogados familiares en CDMX. Divorcio express, pensión alimenticia y guarda y custodia. 15 años de experiencia. Primera consulta GRATIS. ☎ 55 1467 6633.',
           cuerpo, activo='inicio',
           extra_head=JSONLD_LEGAL + jsonld_faq(FAQS_HOME))

# ==================================================== páginas de especialidad
def construir_especialidades():
    for e in ESPECIALIDADES:
        wa_esp = wa(f'Hola, quiero una asesoría en {e["nombre"].lower()}')
        intro = '\n'.join(f'      <p>{p}</p>' for p in e['intro'])
        incluye = '\n'.join(f'        <li>{i}</li>' for i in e['incluye'])
        faqs_html = '\n'.join(f'''      <details>
        <summary>{q}</summary>
        <div class="faq-respuesta"><p>{a}</p></div>
      </details>''' for q, a in e['faqs'])
        otras = '\n'.join(f'            <li><a href="{o["slug"]}.html">{o["nombre"]}</a></li>'
                          for o in ESPECIALIDADES if o['slug'] != e['slug'])
        cuerpo = f'''<div class="page-header">
  <div class="container">
    <nav aria-label="Migas de pan">
      <ol class="breadcrumb">
        <li><a href="index.html">Inicio</a></li>
        <li><a href="especialidades.html">Especialidades</a></li>
        <li aria-current="page">{e['nombre']}</li>
      </ol>
    </nav>
    <h1>{e['titulo']}</h1>
    <p class="subtitulo">{e['corta']}</p>
  </div>
</div>

<section class="seccion" style="padding-top:2.5rem">
  <div class="container contenido">
    <article class="prosa">
{intro}
      <h2>¿Qué incluye este servicio?</h2>
      <ul>
{incluye}
      </ul>
      <h2>¿Cómo trabajamos?</h2>
      <ol>
        <li><strong>Valoración gratuita.</strong> Nos cuentas tu caso por WhatsApp, teléfono o en línea; te decimos si procede y qué vía conviene.</li>
        <li><strong>Estrategia y presupuesto.</strong> Diseñamos la estrategia legal y te damos un presupuesto claro, con plan de pagos si lo necesitas.</li>
        <li><strong>Ejecución.</strong> Presentamos la demanda o el trámite y te informamos de cada avance, sin tecnicismos.</li>
        <li><strong>Resolución.</strong> Acompañamos hasta la sentencia o convenio final y su inscripción, cuando aplica.</li>
      </ol>
      <h2>Preguntas frecuentes</h2>
      <div class="faq">
{faqs_html}
      </div>
      <div class="aviso">Cada asunto es único y requiere un análisis personalizado por parte de nuestros especialistas en derecho familiar. Tras la asesoría inicial, realizamos una evaluación detallada de tu caso y te hacemos llegar una propuesta de honorarios clara y transparente, con opciones de pago accesibles adaptadas a tus necesidades.</div>
    </article>
    <aside class="lateral">
      <div class="widget" style="background:linear-gradient(160deg,var(--rosa-marca),var(--rosa-fuerte));color:#fff">
        <h3 style="color:#fff">Honorarios a tu medida</h3>
        <p style="font-size:.9rem;color:rgba(255,255,255,.92);margin-bottom:1rem">Cada caso es único. Tras tu <strong>primera consulta GRATIS</strong> te entregamos una propuesta de honorarios clara y transparente, con opciones de pago accesibles.</p>
        <a class="btn btn-whatsapp" href="{wa_esp}" target="_blank" rel="noopener">{WA_SVG.format(s=18)} Consulta GRATIS</a>
        <a class="btn btn-claro" href="{TEL_HREF}" style="margin-top:.75rem">{icono('telefono', 18)} {TEL_TXT}</a>
      </div>
      <div class="widget">
        <h3>Otras especialidades</h3>
        <ul>
{otras}
        </ul>
      </div>
    </aside>
  </div>
</section>
''' + cta_final(wa_link=wa_esp)
        pagina(e['slug'] + '.html',
               f"{e['titulo']} | Abogados Familiares CDMX",
               e['meta'], cuerpo,
               extra_head=jsonld_faq(e['faqs']), wa_link=wa_esp)

    # índice de especialidades
    tarjetas = '\n'.join(f'''      <article class="tarjeta tarjeta-esp">
        <div class="icono">{icono(e['icono'])}</div>
        <h3>{e['nombre']}</h3>
        <p>{HOME_DESC.get(e['slug'], e['corta'])}</p>
        <a class="enlace" href="{e['slug']}.html">Conocer más →</a>
      </article>''' for e in ESPECIALIDADES)
    cuerpo = f'''<div class="page-header">
  <div class="container">
    <nav aria-label="Migas de pan">
      <ol class="breadcrumb">
        <li><a href="index.html">Inicio</a></li>
        <li aria-current="page">Especialidades</li>
      </ol>
    </nav>
    <h1>Nuestras Especialidades</h1>
    <p class="subtitulo">Atendemos exclusivamente derecho familiar. Nueve áreas, un solo enfoque: proteger a tu familia.</p>
  </div>
</div>
<section class="seccion" style="padding-top:2.5rem">
  <div class="container">
    <div class="grid-servicios">
{tarjetas}
    </div>
    <p class="nota-precios">Cada caso es único: tras tu primera consulta GRATIS te entregamos una propuesta de honorarios clara, transparente y adaptada a tus necesidades.</p>
  </div>
</section>
''' + cta_final()
    pagina('especialidades.html',
           'Especialidades en Derecho Familiar | Abogados Familiares CDMX',
           'Divorcio, pensión alimenticia, guarda y custodia, patria potestad, violencia familiar, testamentos, convenios, gestoría e interdicción en CDMX. Primera consulta GRATIS.',
           cuerpo)

# ============================================================== BLOG ========
ARTICULOS = [
    dict(slug='cuanto-cuesta-divorcio-cdmx-2026', categoria='Divorcio', icono='corazon',
         titulo='¿Cuánto cuesta un divorcio en CDMX en 2026?',
         extracto='Un divorcio en la Ciudad de México en 2026 puede costar desde $12,500 MXN (express, sin hijos ni bienes) hasta más de $95,000 MXN en casos contenciosos. Te desglosamos honorarios, gastos judiciales y cómo ahorrar.',
         meta='Costos reales de un divorcio en CDMX 2026: desde $12,500 MXN (express) hasta $95,000+ en contenciosos. Desglose de honorarios, gastos y tiempos por tipo de divorcio.',
         cuerpo='''<p>"¿Cuánto me va a costar?" es la primera pregunta de casi todas las personas que quieren divorciarse, y la respuesta honesta es: <strong>depende del tipo de divorcio, de si hay hijos y bienes, y del nivel de conflicto</strong>. Aquí te damos los rangos reales que manejamos en 2026 para que planees con certeza.</p>
<h2>Tabla de costos por tipo de divorcio (2026)</h2>
<table>
  <thead><tr><th>Tipo de divorcio</th><th>Costo aproximado</th><th>Duración típica</th></tr></thead>
  <tbody>
    <tr><td><strong>Express / voluntario</strong> (sin hijos ni bienes)</td><td>$12,500 – $22,500 MXN</td><td>1 – 3 meses</td></tr>
    <tr><td><strong>Voluntario</strong> con hijos y bienes</td><td>$28,000 – $55,000 MXN</td><td>3 – 6 meses</td></tr>
    <tr><td><strong>Incausado</strong> (sin acuerdo del otro cónyuge)</td><td>$35,000 – $65,000 MXN</td><td>4 – 8 meses</td></tr>
    <tr><td><strong>Contencioso</strong> (custodia, pensión o bienes en disputa)</td><td>$55,000 – $95,000+ MXN</td><td>6 – 18 meses</td></tr>
  </tbody>
</table>
<h2>¿Qué incluyen los honorarios?</h2>
<ul>
  <li>Estudio del caso y diseño de la estrategia legal.</li>
  <li>Elaboración de la demanda y del convenio de divorcio.</li>
  <li>Presentación y seguimiento ante el juzgado de lo familiar.</li>
  <li>Audiencias y promociones durante todo el juicio.</li>
  <li>Inscripción de la sentencia en el Registro Civil.</li>
</ul>
<h2>Gastos adicionales a considerar</h2>
<p>Además de los honorarios del abogado, contempla copias certificadas, actas del Registro Civil y, si hay bienes, los costos de liquidación de la sociedad conyugal (avalúos, notario si hay inmuebles). En divorcios contenciosos pueden sumarse periciales (psicológicas, contables).</p>
<h2>¿Cómo ahorrar en tu divorcio?</h2>
<ol>
  <li><strong>Busca el mutuo acuerdo.</strong> Un convenio negociado cuesta una fracción de un juicio contencioso y se resuelve en meses, no años.</li>
  <li><strong>Llega con tus documentos listos.</strong> Acta de matrimonio, actas de nacimiento de los hijos e información de bienes aceleran todo.</li>
  <li><strong>Aprovecha los planes de pago.</strong> En nuestro despacho los juicios pueden iniciarse desde un pago mínimo de $7,500 MXN.</li>
</ol>
<div class="aviso">Los precios de este artículo son ilustrativos y aproximados a 2026; el costo final depende de las particularidades de cada caso. Solicita tu valoración gratuita para un presupuesto exacto.</div>'''),
    dict(slug='que-pasa-si-no-paga-pension', categoria='Pensión Alimenticia', icono='dinero',
         titulo='¿Qué pasa si no pagan la pensión alimenticia?',
         extracto='El incumplimiento tiene consecuencias graves: embargo de bienes y cuentas bancarias, retención directa del salario, inscripción en el RNOA, restricción migratoria y, en casos graves, proceso penal de 3 a 5 años de prisión en CDMX.',
         meta='Consecuencias de no pagar la pensión alimenticia en CDMX: embargo, retención de salario, inscripción en el RNOA, restricciones migratorias y hasta 5 años de prisión.',
         cuerpo='''<p>La pensión alimenticia no es opcional: es una obligación legal cuyo incumplimiento tiene consecuencias civiles, administrativas y hasta penales. Si te deben pensión —o si te están reclamando una— esto es lo que debes saber en 2026.</p>
<h2>1. Embargo de bienes y cuentas</h2>
<p>El juez familiar puede ordenar el <strong>embargo de bienes, cuentas bancarias e inversiones</strong> del deudor para garantizar y cubrir las pensiones vencidas. El embargo puede recaer también sobre el aguinaldo, la prima vacacional y otras prestaciones.</p>
<h2>2. Retención directa del salario</h2>
<p>La medida más efectiva: el juez ordena al patrón <strong>descontar la pensión directamente de la nómina</strong> y entregarla al acreedor. El patrón que desobedece incurre en responsabilidad.</p>
<h2>3. Inscripción en el RNOA</h2>
<p>El <strong>Registro Nacional de Obligaciones Alimentarias (RNOA)</strong> inscribe a los deudores alimentarios morosos. Estar en el registro acarrea restricciones serias: impedimentos para obtener licencias y pasaporte en ciertos supuestos, para participar en cargos públicos, e incluso para celebrar ciertos actos ante notario. Además, el registro es consultable en procesos de adopción y custodia.</p>
<h2>4. Restricción migratoria</h2>
<p>En determinados casos, el juez puede dictar <strong>alerta migratoria</strong> para impedir que el deudor abandone el país sin garantizar el pago de los alimentos.</p>
<h2>5. Proceso penal</h2>
<p>El incumplimiento reiterado e injustificado constituye el <strong>delito de incumplimiento de obligaciones alimentarias</strong>, con pena de <strong>3 a 5 años de prisión</strong> en CDMX, además de la suspensión de derechos de familia. El pago posterior no siempre extingue la acción penal.</p>
<h2>¿Qué hacer si no te pagan?</h2>
<ol>
  <li>Documenta los pagos incumplidos (estados de cuenta, mensajes).</li>
  <li>Solicita al juez la ejecución de la sentencia o convenio: embargo y retención de nómina.</li>
  <li>Pide la inscripción del deudor en el RNOA.</li>
  <li>Valora la denuncia penal en casos graves y reiterados.</li>
</ol>
<div class="aviso">Cada caso es distinto. En tu valoración gratuita revisamos tu convenio o sentencia y te decimos exactamente qué medidas proceden.</div>'''),
    dict(slug='custodia-compartida-mexico-2026', categoria='Custodia', icono='familia',
         titulo='Custodia compartida en México 2026',
         extracto='La custodia compartida gana relevancia en México. Aunque el Código Civil de CDMX no la regula como figura autónoma, la SCJN permite a los jueces otorgarla cuando beneficia al menor. Requisitos: acuerdo entre padres, domicilios cercanos, buena comunicación y estabilidad.',
         meta='Custodia compartida en México 2026: qué dice la SCJN, requisitos que valoran los jueces de CDMX y cuándo conviene solicitarla. Guía práctica actualizada.',
         cuerpo='''<p>Cada vez más padres y madres preguntan por la <strong>custodia compartida</strong>: un esquema donde ambos progenitores participan de manera equilibrada en la vida cotidiana de los hijos. Te explicamos cómo funciona realmente en CDMX en 2026.</p>
<h2>¿Qué es la custodia compartida?</h2>
<p>Es la distribución equilibrada de la convivencia y el cuidado del menor entre ambos padres tras la separación: semanas o quincenas alternadas, o esquemas a la medida. No debe confundirse con la <strong>patria potestad</strong> (que normalmente conservan ambos padres) ni con el <strong>régimen de visitas</strong> tradicional.</p>
<h2>¿Está en la ley?</h2>
<p>El Código Civil para la Ciudad de México no regula la custodia compartida como figura autónoma. Sin embargo, la <strong>Suprema Corte de Justicia de la Nación (SCJN)</strong> ha sostenido que los jueces pueden decretarla cuando resulte benéfica para el menor, pues el criterio rector de toda decisión es el <strong>interés superior de la infancia</strong>.</p>
<h2>Requisitos que valoran los jueces</h2>
<ul>
  <li><strong>Acuerdo y disposición de ambos padres</strong> para cooperar en la crianza.</li>
  <li><strong>Domicilios cercanos</strong>, que permitan continuidad escolar y social del menor.</li>
  <li><strong>Buena comunicación</strong> entre los progenitores (o al menos funcional).</li>
  <li><strong>Estabilidad</strong>: horarios, vivienda y entorno adecuados en ambas casas.</li>
  <li>La <strong>opinión del menor</strong>, valorada según su edad y madurez.</li>
</ul>
<h2>¿Cuándo conviene (y cuándo no)?</h2>
<p>Funciona muy bien cuando ambos padres son corresponsables y viven cerca. No es recomendable cuando hay violencia familiar, conflicto extremo o distancias que obliguen al menor a cambiar constantemente de escuela o rutina.</p>
<h2>¿Y la pensión alimenticia?</h2>
<p>La custodia compartida <strong>no elimina automáticamente la pensión</strong>: si existe diferencia de ingresos entre los padres, el juez puede fijar una pensión compensatoria para mantener condiciones de vida equivalentes en ambos hogares.</p>
<div class="aviso">¿Quieres proponer una custodia compartida o te la están proponiendo? Agenda tu valoración gratuita y te decimos si tu caso reúne los requisitos.</div>'''),
    dict(slug='proteger-hijos-durante-divorcio', categoria='Custodia', icono='escudo',
         titulo='Cómo proteger a tus hijos durante un divorcio',
         extracto='El interés superior del menor guía toda decisión de custodia, pensión y régimen de visitas. Te explicamos cómo documentar tu capacidad parental, qué evalúa el juez y cómo evitar la alienación parental.',
         meta='Guía para proteger a tus hijos durante un divorcio en CDMX: qué evalúa el juez, cómo documentar tu capacidad parental y cómo prevenir la alienación parental.',
         cuerpo='''<p>Un divorcio termina con el matrimonio, no con la familia. La forma en que los padres manejen el proceso determina, en gran medida, el impacto emocional en los hijos. Esta guía resume lo que evalúa el juez y lo que puedes hacer desde hoy.</p>
<h2>El principio rector: interés superior del menor</h2>
<p>Toda decisión sobre <strong>custodia, pensión alimenticia y régimen de visitas</strong> se toma conforme al interés superior del menor: su seguridad, salud, educación, estabilidad emocional y derecho a convivir con ambos padres. No se trata de "ganarle" al otro, sino de demostrar quién ofrece las mejores condiciones.</p>
<h2>Qué evalúa el juez</h2>
<ul>
  <li><strong>Capacidad parental:</strong> participación real en la crianza (escuela, médico, rutinas).</li>
  <li><strong>Estabilidad:</strong> vivienda adecuada, horarios compatibles, red de apoyo familiar.</li>
  <li><strong>Entorno libre de violencia:</strong> antecedentes de violencia familiar pesan de forma determinante.</li>
  <li><strong>Disposición a facilitar la convivencia</strong> del menor con el otro progenitor.</li>
  <li><strong>La opinión del menor</strong>, escuchada conforme a su edad y madurez.</li>
</ul>
<h2>Cómo documentar tu capacidad parental</h2>
<ol>
  <li>Guarda constancias escolares y médicas donde aparezcas como responsable.</li>
  <li>Conserva comunicaciones (mensajes, correos) que muestren tu participación cotidiana.</li>
  <li>Mantén un registro de gastos de los hijos: colegiaturas, ropa, salud, actividades.</li>
  <li>Evita exponer a los hijos al conflicto: no los uses como mensajeros ni testigos.</li>
</ol>
<h2>Alienación parental: qué es y cómo evitarla</h2>
<p>Hablar mal del otro progenitor frente a los hijos, obstaculizar las convivencias o manipular su afecto daña al menor y <strong>puede revertirse en tu contra en el juicio</strong>: los jueces valoran negativamente al progenitor que obstaculiza el vínculo con el otro. Si tú eres quien la sufre, documenta los episodios y solicita la intervención del juez.</p>
<h2>Recomendaciones finales</h2>
<ul>
  <li>Prioriza los acuerdos: un convenio de custodia y visitas negociado protege más a los hijos que una sentencia impuesta.</li>
  <li>Considera apoyo psicológico para los hijos durante el proceso.</li>
  <li>Asesórate desde el inicio: las decisiones de los primeros meses (quién se queda en casa, rutinas provisionales) influyen en la resolución final.</li>
</ul>
<div class="aviso">En tu valoración gratuita analizamos tu situación y diseñamos una estrategia que proteja primero a tus hijos — y también tus derechos.</div>'''),
]

def construir_blog():
    cards = '\n'.join(f'''      <article class="tarjeta tarjeta-blog">
        <div class="portada">{icono(a['icono'], 44)}</div>
        <div class="cuerpo">
          <span class="categoria">{a['categoria']}</span>
          <h3><a href="blog/{a['slug']}.html" style="color:inherit">{a['titulo']}</a></h3>
          <p>{a['extracto']}</p>
          <a class="enlace" href="blog/{a['slug']}.html">Leer más →</a>
        </div>
      </article>''' for a in ARTICULOS)
    cuerpo = f'''<div class="page-header">
  <div class="container">
    <nav aria-label="Migas de pan">
      <ol class="breadcrumb">
        <li><a href="index.html">Inicio</a></li>
        <li aria-current="page">Blog</li>
      </ol>
    </nav>
    <h1>Blog Jurídico</h1>
    <p class="subtitulo">Guías legales de derecho familiar en CDMX 2026: información clara para tomar mejores decisiones.</p>
  </div>
</div>
<section class="seccion" style="padding-top:2.5rem">
  <div class="container">
    <div class="grid-blog">
{cards}
    </div>
  </div>
</section>
''' + cta_final()
    pagina('blog.html',
           'Blog Jurídico | Abogados Familiares CDMX',
           'Guías legales de derecho familiar en CDMX 2026: divorcio, pensión alimenticia, custodia, testamentos y más. Escrito por abogados especialistas.',
           cuerpo, activo='blog')

    for a in ARTICULOS:
        relacionados = '\n'.join(
            f'            <li><a href="{o["slug"]}.html">{o["titulo"]}</a></li>'
            for o in ARTICULOS if o['slug'] != a['slug'])
        cuerpo = f'''<div class="page-header">
  <div class="container">
    <nav aria-label="Migas de pan">
      <ol class="breadcrumb">
        <li><a href="../index.html">Inicio</a></li>
        <li><a href="../blog.html">Blog</a></li>
        <li aria-current="page">{a['titulo']}</li>
      </ol>
    </nav>
    <span class="categoria" style="display:inline-block;background:var(--rosa-100);color:var(--rosa-fuerte);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;padding:.3rem .9rem;border-radius:999px;margin-bottom:.75rem">{a['categoria']}</span>
    <h1>{a['titulo']}</h1>
    <p class="meta-articulo">Por el equipo de Abogados Familiares CDMX · Actualizado: junio de 2026</p>
  </div>
</div>
<section class="seccion" style="padding-top:2.5rem">
  <div class="container contenido">
    <article class="prosa">
{a['cuerpo']}
    </article>
    <aside class="lateral">
      <div class="widget" style="background:linear-gradient(160deg,var(--rosa-marca),var(--rosa-fuerte));color:#fff">
        <h3 style="color:#fff">¿Tienes un caso similar?</h3>
        <p style="color:rgba(255,255,255,.92)">Tu primera consulta es gratis y sin compromiso.</p>
        <a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">{WA_SVG.format(s=18)} Consulta GRATIS</a>
      </div>
      <div class="widget">
        <h3>Más artículos</h3>
        <ul>
{relacionados}
        </ul>
      </div>
    </aside>
  </div>
</section>
''' + cta_final('../')
        pagina('blog/' + a['slug'] + '.html',
               f"{a['titulo']} | Abogados Familiares CDMX",
               a['meta'], cuerpo)

# =========================================================== CONTACTO =======
def construir_contacto():
    cuerpo = f'''<div class="page-header">
  <div class="container">
    <nav aria-label="Migas de pan">
      <ol class="breadcrumb">
        <li><a href="index.html">Inicio</a></li>
        <li aria-current="page">Contacto</li>
      </ol>
    </nav>
    <h1>Contacto</h1>
    <p class="subtitulo">Déjanos tus datos y te contactamos en menos de 2 horas hábiles. Tu primera consulta es GRATIS.</p>
  </div>
</div>
<section class="seccion" style="padding-top:2.5rem">
  <div class="container form-grid">
    <div class="formulario">
      <h2 style="font-size:1.4rem">Recibe asesoría gratuita</h2>
      <form action="{FORMSPREE}" method="POST">
        <label for="f-nombre">Nombre completo</label>
        <input type="text" id="f-nombre" name="nombre" placeholder="Nombre completo" autocomplete="name" required>
        <label for="f-telefono">Teléfono / WhatsApp</label>
        <input type="tel" id="f-telefono" name="telefono" placeholder="Teléfono / WhatsApp" autocomplete="tel" required>
        <label for="f-email">Correo electrónico</label>
        <input type="email" id="f-email" name="email" placeholder="Correo electrónico" autocomplete="email" required>
        <label for="f-tema">¿En qué podemos ayudarte?</label>
        <select id="f-tema" name="tema" required>
          <option value="" disabled selected>Selecciona un tema</option>
          <option>Divorcio</option>
          <option>Pensión alimenticia</option>
          <option>Guarda y custodia</option>
          <option>Patria potestad</option>
          <option>Violencia familiar</option>
          <option>Testamentos y sucesiones</option>
          <option>Otro</option>
        </select>
        <label for="f-mensaje">Mensaje (opcional)</label>
        <textarea id="f-mensaje" name="mensaje" placeholder="Cuéntanos brevemente tu caso (opcional)"></textarea>
        <input type="hidden" name="_subject" value="Nueva consulta desde el sitio web (contacto)">
        <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
        <p class="consentimiento">Al enviar este formulario aceptas nuestro <a href="aviso-de-privacidad.html">Aviso de Privacidad</a>. Tus datos solo se usan para contactarte sobre tu consulta.</p>
        <button type="submit" class="btn btn-primario btn-grande">Recibir Asesoría</button>
        <p class="form-estado" role="status" aria-live="polite"></p>
      </form>
      <p style="text-align:center;margin:1.25rem 0 0"><a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">{WA_SVG.format(s=18)} Prefiero WhatsApp</a></p>
    </div>
    <div>
      <ul class="contacto-datos">
        <li><span class="icono">{icono('ubicacion', 22)}</span><div><b>Ubicación</b><span>{DIRECCION}.<br>A 2 min del Metro Revolución (Línea 2).</span></div></li>
        <li><span class="icono">{icono('telefono', 22)}</span><div><b>Teléfono</b><a href="{TEL_HREF}">{TEL_TXT}</a></div></li>
        <li><span class="icono">{icono('correo', 22)}</span><div><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
        <li><span class="icono">{icono('reloj', 22)}</span><div><b>Horario</b><span>Lun–Vie 9:00–19:00 · Sáb 10:00–14:00<br>Urgencias por violencia familiar: 24/7</span></div></li>
      </ul>
      <div class="mapa">
        <iframe src="{MAPS_EMBED}" title="Mapa de la ubicación del despacho — Abogados Familiares CDMX, Col. Tabacalera, CDMX" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
          <p style="margin:.6rem 0 0;text-align:center"><a href="{MAPS_LINK}" target="_blank" rel="noopener">Ver en Google Maps →</a></p>
      </div>
    </div>
  </div>
</section>
'''
    pagina('contacto.html',
           'Contacto | Abogados Familiares CDMX',
           'Agenda tu consulta GRATIS con abogados familiares en CDMX. ☎ 55 1467 6633. Be Grand Downtown Reforma, Col. Tabacalera, a 2 min del Metro Revolución.',
           cuerpo, activo='contacto', extra_head=JSONLD_LEGAL)

# ============================================================ LEGALES ========
def construir_legales():
    aviso = f'''<div class="page-header">
  <div class="container">
    <nav aria-label="Migas de pan">
      <ol class="breadcrumb">
        <li><a href="index.html">Inicio</a></li>
        <li aria-current="page">Aviso de Privacidad</li>
      </ol>
    </nav>
    <h1>Aviso de Privacidad</h1>
    <p class="subtitulo">Última actualización: junio de 2026</p>
  </div>
</div>
<section class="seccion" style="padding-top:2.5rem">
  <div class="container" style="max-width:820px">
    <article class="prosa">
      <div class="aviso"><strong>Borrador para revisión legal.</strong> Este documento es un placeholder elaborado conforme a la Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP) y debe ser revisado y validado por un abogado del despacho antes de su publicación definitiva.</div>
      <h2>1. Identidad y domicilio del responsable</h2>
      <p><strong>Abogados Familiares CDMX</strong>, con domicilio en {DIRECCION}, es el responsable del tratamiento de tus datos personales conforme al presente aviso.</p>
      <h2>2. Datos personales que recabamos</h2>
      <p>A través de nuestro formulario de contacto, llamadas telefónicas y WhatsApp podemos recabar: nombre completo, número de teléfono, correo electrónico y la descripción del caso o asunto legal que nos compartas. No recabamos datos personales sensibles a través del sitio web.</p>
      <h2>3. Finalidades del tratamiento</h2>
      <ul>
        <li>Contactarte para atender tu solicitud de asesoría.</li>
        <li>Agendar consultas y citas.</li>
        <li>Dar seguimiento a tu caso cuando contrates nuestros servicios.</li>
        <li>De forma secundaria, y solo con tu consentimiento, enviarte información sobre nuestros servicios.</li>
      </ul>
      <h2>4. Derechos ARCO</h2>
      <p>Tienes derecho a <strong>Acceder</strong>, <strong>Rectificar</strong> y <strong>Cancelar</strong> tus datos personales, así como a <strong>Oponerte</strong> a su tratamiento (derechos ARCO). Para ejercerlos, envía tu solicitud al correo <a href="mailto:{EMAIL}">{EMAIL}</a>, indicando tu nombre, el derecho que deseas ejercer y los datos de contacto para darte respuesta. Responderemos en los plazos previstos por la LFPDPPP.</p>
      <h2>5. Limitación de uso o divulgación</h2>
      <p>Puedes solicitar en cualquier momento que limitemos el uso o divulgación de tus datos escribiendo al correo indicado en el punto anterior. No transferimos tus datos personales a terceros sin tu consentimiento, salvo las excepciones previstas por la ley.</p>
      <h2>6. Uso de servicios de terceros</h2>
      <p>El formulario de este sitio se procesa a través de Formspree, y el sitio se aloja en GitHub Pages; ambos proveedores pueden tratar datos técnicos (como tu dirección IP) conforme a sus propias políticas de privacidad. Los mapas se muestran mediante Google Maps.</p>
      <h2>7. Cambios al aviso de privacidad</h2>
      <p>Cualquier modificación al presente aviso se publicará en esta misma página, indicando la fecha de última actualización.</p>
    </article>
  </div>
</section>
'''
    pagina('aviso-de-privacidad.html',
           'Aviso de Privacidad | Abogados Familiares CDMX',
           'Aviso de privacidad de Abogados Familiares CDMX conforme a la LFPDPPP: datos que recabamos, finalidades del tratamiento y derechos ARCO.',
           aviso)

    terminos = f'''<div class="page-header">
  <div class="container">
    <nav aria-label="Migas de pan">
      <ol class="breadcrumb">
        <li><a href="index.html">Inicio</a></li>
        <li aria-current="page">Términos y Condiciones</li>
      </ol>
    </nav>
    <h1>Términos y Condiciones</h1>
    <p class="subtitulo">Última actualización: junio de 2026</p>
  </div>
</div>
<section class="seccion" style="padding-top:2.5rem">
  <div class="container" style="max-width:820px">
    <article class="prosa">
      <div class="aviso"><strong>Borrador para revisión legal.</strong> Este documento es un placeholder y debe ser revisado y validado por un abogado del despacho antes de su publicación definitiva.</div>
      <h2>1. Alcance del sitio</h2>
      <p>El contenido de este sitio web tiene fines exclusivamente informativos y de divulgación general. <strong>No constituye asesoría legal formal</strong> ni crea una relación abogado–cliente; dicha relación se establece únicamente mediante la contratación expresa de nuestros servicios.</p>
      <h2>2. Precios ilustrativos</h2>
      <p>Todos los precios y rangos publicados en este sitio son <strong>ilustrativos y aproximados</strong>. El costo final de cualquier servicio depende de las particularidades de cada caso y se confirma por escrito antes de la contratación.</p>
      <h2>3. Propiedad intelectual</h2>
      <p>El contenido del sitio (textos, logotipo, diseño y materiales) es propiedad de Abogados Familiares CDMX o se utiliza con autorización. Queda prohibida su reproducción con fines comerciales sin consentimiento previo y por escrito.</p>
      <h2>4. Limitación de responsabilidad</h2>
      <p>La información publicada se actualiza periódicamente, pero la legislación y los criterios judiciales cambian; no garantizamos que todo el contenido refleje la normativa vigente al momento de tu consulta. Las decisiones que tomes con base en la información del sitio son tu responsabilidad; te recomendamos siempre buscar asesoría personalizada.</p>
      <h2>5. Enlaces y servicios de terceros</h2>
      <p>El sitio puede contener enlaces a servicios de terceros (WhatsApp, Google Maps, Formspree, Calendly). No somos responsables del contenido ni de las políticas de dichos servicios.</p>
      <h2>6. Legislación aplicable</h2>
      <p>Estos términos se rigen por la legislación de la Ciudad de México y demás leyes federales aplicables de los Estados Unidos Mexicanos. Cualquier controversia se someterá a los tribunales competentes de la Ciudad de México.</p>
      <h2>7. Contacto</h2>
      <p>Para cualquier duda sobre estos términos: <a href="mailto:{EMAIL}">{EMAIL}</a> · Tel. <a href="{TEL_HREF}">{TEL_TXT}</a>.</p>
    </article>
  </div>
</section>
'''
    pagina('terminos-y-condiciones.html',
           'Términos y Condiciones | Abogados Familiares CDMX',
           'Términos y condiciones de uso del sitio web de Abogados Familiares CDMX: alcance informativo, precios ilustrativos, propiedad intelectual y legislación aplicable.',
           terminos)

# ====================================================== 404 y GRACIAS =======
def construir_extra():
    cuerpo404 = f'''<section class="pagina-centrada container">
  <p class="numero">404</p>
  <h1>Página no encontrada</h1>
  <p style="color:var(--texto-suave);max-width:480px;margin-inline:auto">La página que buscas no existe o cambió de dirección. Pero estamos aquí para ayudarte con tu caso.</p>
  <div class="hero-ctas" style="justify-content:center;margin-top:1.5rem">
    <a class="btn btn-primario" href="index.html">Ir al inicio</a>
    <a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">{WA_SVG.format(s=18)} Consulta GRATIS</a>
  </div>
</section>
'''
    pagina('404.html', 'Página no encontrada | Abogados Familiares CDMX',
           'La página que buscas no existe. Visita el inicio o contáctanos para recibir asesoría legal familiar en CDMX.', cuerpo404)

    cuerpo_gracias = f'''<section class="pagina-centrada container">
  <p class="numero" style="font-size:4rem">✓</p>
  <h1>¡Gracias por tu mensaje!</h1>
  <p style="color:var(--texto-suave);max-width:520px;margin-inline:auto">Recibimos tu consulta y te contactaremos en menos de <strong>2 horas hábiles</strong>. Si tu asunto es urgente, escríbenos directo por WhatsApp.</p>
  <div class="hero-ctas" style="justify-content:center;margin-top:1.5rem">
    <a class="btn btn-whatsapp" href="{WA}" target="_blank" rel="noopener">{WA_SVG.format(s=18)} Abrir WhatsApp</a>
    <a class="btn btn-secundario" href="index.html">Volver al inicio</a>
  </div>
</section>
'''
    pagina('gracias.html', 'Gracias por tu consulta | Abogados Familiares CDMX',
           'Recibimos tu consulta. Te contactaremos en menos de 2 horas hábiles. Abogados familiares en CDMX.', cuerpo_gracias)

# ============================================== robots / sitemap / README ===
def construir_seo():
    os.makedirs(PUBLICO, exist_ok=True)
    with open(os.path.join(PUBLICO, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write('User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n' % SITE)
    print('✓ robots.txt')

    rutas = (['', 'especialidades.html'] +
             [e['slug'] + '.html' for e in ESPECIALIDADES] +
             ['blog.html'] +
             ['blog/' + a['slug'] + '.html' for a in ARTICULOS] +
             ['contacto.html', 'aviso-de-privacidad.html', 'terminos-y-condiciones.html'])
    urls = '\n'.join(
        '  <url>\n    <loc>%s/%s</loc>\n    <lastmod>2026-06-12</lastmod>\n  </url>' % (SITE, r)
        for r in rutas)
    with open(os.path.join(PUBLICO, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + urls + '\n</urlset>\n')
    print('✓ sitemap.xml')

if __name__ == '__main__':
    construir_home()
    construir_especialidades()
    construir_blog()
    construir_contacto()
    construir_legales()
    construir_extra()
    construir_seo()
    print('\nListo: sitio generado en', RAIZ)
