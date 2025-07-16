document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('addressToggleBtn');
  const dropdown = document.getElementById('addressDropdown');
  const cityBtns = document.querySelectorAll('.city-btn');
  const mapIframe = document.querySelector('.address-map-real iframe');
  const closeDropdownBtn = document.getElementById('closeDropdownBtn');

  // Показывает адреса выбранного города, подсвечивает первый адрес и выставляет карту
  function showCity(btn) {
    const city = btn.getAttribute('data-city');

    document.querySelectorAll('.city-addresses').forEach(section => {
      section.classList.remove('active');
      section.hidden = true;
    });
    cityBtns.forEach(b => b.setAttribute('aria-expanded', 'false'));

    btn.setAttribute('aria-expanded', 'true');

    const section = document.querySelector(`.city-addresses[data-city-addresses="${city}"]`);
    if (!section) return;

    section.classList.add('active');
    section.hidden = false;

    const firstAddress = section.querySelector('.address-block');
    if (firstAddress) {
      highlightAddress(firstAddress);
      updateMap(firstAddress.getAttribute('data-map-src'));
    }
  }

  // Обновляет src iframe карты с минимизацией моргания
  function updateMap(src) {
    if (!src || mapIframe.src === src) return;

    // Скрываем iframe перед сменой src
    mapIframe.style.visibility = 'hidden';
    mapIframe.style.opacity = '0';

    // Обработчик загрузки карты — показываем iframe обратно
    function onLoadHandler() {
      mapIframe.style.transition = 'opacity 0.3s ease';
      mapIframe.style.opacity = '1';
      mapIframe.style.visibility = 'visible';
      mapIframe.removeEventListener('load', onLoadHandler);
    }
    mapIframe.addEventListener('load', onLoadHandler);

    // Меняем src
    mapIframe.src = src;
  }

  // Подсвечивает выбранный адрес
  function highlightAddress(addrEl) {
    document.querySelectorAll('.address-block').forEach(block => {
      block.classList.remove('active');
    });
    addrEl.classList.add('active');
  }

  toggleBtn.addEventListener('click', () => {
    const isActive = dropdown.classList.toggle('active');
    toggleBtn.setAttribute('aria-expanded', isActive);

    if (isActive) {
      cityBtns.forEach(b => b.setAttribute('aria-expanded', 'false'));
      document.querySelectorAll('.city-addresses').forEach(ca => {
        ca.classList.remove('active');
        ca.hidden = true;
      });
    }
  });

  cityBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      showCity(btn);
    });
  });

  document.querySelectorAll('.address-block').forEach(block => {
    block.style.cursor = 'pointer';
    block.addEventListener('click', () => {
      updateMap(block.getAttribute('data-map-src'));
      highlightAddress(block);
    });
  });

  closeDropdownBtn.addEventListener('click', () => {
    dropdown.classList.remove('active');
    toggleBtn.setAttribute('aria-expanded', 'false');
    document.querySelectorAll('.city-addresses').forEach(ca => {
      ca.classList.remove('active');
      ca.hidden = true;
    });
    cityBtns.forEach(btn => btn.setAttribute('aria-expanded', 'false'));
  });

  document.addEventListener('click', e => {
    if (!dropdown.contains(e.target) && !toggleBtn.contains(e.target) && !closeDropdownBtn.contains(e.target)) {
      dropdown.classList.remove('active');
      toggleBtn.setAttribute('aria-expanded', 'false');
      document.querySelectorAll('.city-addresses').forEach(ca => {
        ca.classList.remove('active');
        ca.hidden = true;
      });
      cityBtns.forEach(btn => btn.setAttribute('aria-expanded', 'false'));
    }
  });

  // Инициализация: показать первый город и адрес
  if (cityBtns.length > 0) {
    showCity(cityBtns[0]);
  }

  // Аппаратные ускорения для плавности справа в CSS:
  // .address-map-real { transform: translate3d(0,0,0); }
});
