document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('addressToggleBtn');
  const dropdown = document.getElementById('addressDropdown');
  const cityBtns = document.querySelectorAll('.city-btn');
  const mapIframe = document.querySelector('.address-map-real iframe');

  // Показать город и обновить карту
  function showCity(btn) {
    const city = btn.getAttribute('data-city');

    // Деактивируем все секции адресов и сбрасываем aria-expanded
    document.querySelectorAll('.city-addresses').forEach(section => {
      section.classList.remove('active');
    });
    cityBtns.forEach(b => b.setAttribute('aria-expanded', 'false'));

    // Активируем выбранный город
    btn.setAttribute('aria-expanded', 'true');
    const section = document.querySelector(`.city-addresses[data-city-addresses="${city}"]`);
    if (section) {
      section.classList.add('active');

      // Показываем первый адрес данного города и ставим карту по нему
      const firstAddress = section.querySelector('.address-block');
      if (firstAddress) {
        updateMap(firstAddress.getAttribute('data-map-src'));
        // Также выделим этот адрес активным (опционально)
        highlightAddress(firstAddress);
      }
    }
  }

  // Обновление src iframe карты
  function updateMap(src) {
    if (mapIframe && src) {
      mapIframe.src = src;
    }
  }

  // Выделение активного адреса (добавим класс и уберём у остальных)
  function highlightAddress(activeAddress) {
    document.querySelectorAll('.address-block').forEach(block => {
      block.classList.remove('active');
    });
    activeAddress.classList.add('active');
  }

  // Скрыть/показать весь список адресов при клике на кнопку
  toggleBtn.addEventListener('click', () => {
    const isActive = dropdown.classList.toggle('active');
    toggleBtn.setAttribute('aria-expanded', isActive);

    if (isActive) {
      // При открытии показываем дефолтный город — Минск
      showCity(cityBtns[0]);
    }
  });

  // Обработка клика по кнопке выбора города
  cityBtns.forEach(btn => {
    btn.addEventListener('click', () => showCity(btn));
  });

  // Обработка клика по отдельному адресу
  document.querySelectorAll('.address-block').forEach(block => {
    block.style.cursor = 'pointer';
    block.addEventListener('click', () => {
      updateMap(block.getAttribute('data-map-src'));
      highlightAddress(block);


    });
  });

  // При загрузке страницы сразу показываем Минск и первый адрес с картой
  if (cityBtns.length) {
    showCity(cityBtns[0]);
  }

  // Закрываем дропдаун если клик вне его
  document.addEventListener('click', (e) => {
    if (!dropdown.contains(e.target) && !toggleBtn.contains(e.target)) {
      dropdown.classList.remove('active');
      toggleBtn.setAttribute('aria-expanded', 'false');
    }
  });
});
