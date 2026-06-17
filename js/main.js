/* Abogados Familiares CDMX — main.js (vanilla, sin dependencias) */
(function () {
  'use strict';

  /* ---------- Menú móvil (hamburguesa) ---------- */
  var navToggle = document.querySelector('.nav-toggle');
  var navMenu = document.querySelector('.nav-menu');
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', function () {
      var abierto = navMenu.classList.toggle('abierto');
      navToggle.setAttribute('aria-expanded', abierto ? 'true' : 'false');
    });
  }

  /* ---------- Dropdown de especialidades ---------- */
  document.querySelectorAll('.dropdown').forEach(function (dd) {
    var toggle = dd.querySelector('.dropdown-toggle');
    if (!toggle) return;

    function cerrar() {
      dd.classList.remove('abierto');
      toggle.setAttribute('aria-expanded', 'false');
    }
    toggle.addEventListener('click', function (e) {
      e.stopPropagation();
      var abierto = dd.classList.toggle('abierto');
      toggle.setAttribute('aria-expanded', abierto ? 'true' : 'false');
    });
    document.addEventListener('click', function (e) {
      if (!dd.contains(e.target)) cerrar();
    });
    dd.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { cerrar(); toggle.focus(); }
    });
  });

  /* ---------- Navbar con sombra al hacer scroll ---------- */
  var header = document.querySelector('.header');
  if (header) {
    var actualizarSombra = function () {
      header.classList.toggle('scrolled', window.scrollY > 40);
    };
    window.addEventListener('scroll', actualizarSombra, { passive: true });
    actualizarSombra();
  }

  /* ---------- Carrusel de testimonios ---------- */
  document.querySelectorAll('.carrusel').forEach(function (carrusel) {
    var pista = carrusel.querySelector('.carrusel-pista');
    var items = pista ? pista.children : [];
    if (!pista || items.length < 2) return;

    var actual = 0;
    var puntosWrap = carrusel.querySelector('.carrusel-puntos');
    var puntos = [];

    for (var i = 0; i < items.length; i++) {
      var p = document.createElement('button');
      p.type = 'button';
      p.className = 'carrusel-punto';
      p.setAttribute('aria-label', 'Ir al testimonio ' + (i + 1));
      (function (idx) {
        p.addEventListener('click', function () { ir(idx, true); });
      })(i);
      puntosWrap.appendChild(p);
      puntos.push(p);
    }

    function ir(idx, manual) {
      actual = (idx + items.length) % items.length;
      pista.style.transform = 'translateX(-' + (actual * 100) + '%)';
      puntos.forEach(function (pt, j) {
        pt.setAttribute('aria-current', j === actual ? 'true' : 'false');
      });
      if (manual) reiniciar();
    }

    var timer = null;
    function reiniciar() {
      if (timer) clearInterval(timer);
      if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        timer = setInterval(function () { ir(actual + 1); }, 6000);
      }
    }

    carrusel.querySelector('.carrusel-prev').addEventListener('click', function () { ir(actual - 1, true); });
    carrusel.querySelector('.carrusel-next').addEventListener('click', function () { ir(actual + 1, true); });
    ir(0);
    reiniciar();
  });

  /* ---------- Formulario de captación (Formspree, envío AJAX) ---------- */
  var form = document.querySelector('.formulario form');
  if (form) {
    var estado = form.querySelector('.form-estado') || document.createElement('p');
    estado.className = 'form-estado';
    form.appendChild(estado);

    form.addEventListener('submit', function (e) {
      // si el action sigue siendo el placeholder, no interceptar (modo demo)
      if (form.action.indexOf('TU_ID_FORMSPREE') !== -1) {
        e.preventDefault();
        estado.className = 'form-estado error';
        estado.textContent = 'El formulario aún no está conectado. Escríbenos por WhatsApp: 56 2082 9905.';
        return;
      }
      e.preventDefault();
      var boton = form.querySelector('button[type="submit"]');
      boton.disabled = true;
      estado.className = 'form-estado';
      estado.textContent = '';

      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      }).then(function (res) {
        if (res.ok) {
          form.reset();
          estado.className = 'form-estado exito';
          estado.textContent = '✓ ¡Gracias! Recibimos tu consulta. Te contactaremos en menos de 2 horas hábiles.';
        } else {
          throw new Error('respuesta no OK');
        }
      }).catch(function () {
        estado.className = 'form-estado error';
        estado.textContent = 'No pudimos enviar el formulario. Inténtalo de nuevo o escríbenos por WhatsApp: 56 2082 9905.';
      }).finally(function () {
        boton.disabled = false;
      });
    });
  }

  /* ---------- Año dinámico en el footer ---------- */
  document.querySelectorAll('[data-anio]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
