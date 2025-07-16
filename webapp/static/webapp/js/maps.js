document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('addressToggleBtn');
  const dropdown = document.getElementById('addressDropdown');
  const cityBtns = document.querySelectorAll('.city-btn');
  const addressBlocks = document.querySelectorAll('.address-block');
  const mapIframe = document.querySelector('.address-map-real iframe');

  let scrollPosition = 0;

  toggleBtn.addEventListener('click', () => {
    scrollPosition = window.pageYOffset || document.documentElement.scrollTop;

    const isActive = dropdown.classList.toggle('active');
    toggleBtn.setAttribute('aria-expanded', isActive);

    if (isActive && cityBtns.length) {
      showCity(cityBtns[0]);
    }

    window.scrollTo({ top: scrollPosition, behavior: 'auto' });
  });

  cityBtns.forEach(btn => {
    btn.addEventListener('click', () => showCity(btn));
  });

  function showCity(btn) {
    const city = btn.getAttribute('data-city');

    document.querySelectorAll('.city-addresses').forEach(section => {
      section.classList.remove('active');
    });

    cityBtns.forEach(b => b.setAttribute('aria-expanded', 'false'));

    btn.setAttribute('aria-expanded', 'true');
    const section = document.querySelector(`.city-addresses[data-city-addresses="${city}"]`);
    if (section) section.classList.add('active');
  }

  addressBlocks.forEach(block => {
    block.style.cursor = 'pointer';
    block.addEventListener('click', () => {
      const mapSrc = block.getAttribute('data-map-src');
      if (!mapSrc) return;

      mapIframe.src = mapSrc;


      const mapSection = document.querySelector('.address-map-real');
      if (mapSection) {
        mapSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ✅ Закрытие при клике вне блока
  document.addEventListener('click', (e) => {
    const isClickInside = dropdown.contains(e.target) || toggleBtn.contains(e.target);
    if (!isClickInside && dropdown.classList.contains('active')) {
      dropdown.classList.remove('active');
      toggleBtn.setAttribute('aria-expanded', 'false');
    }
  });

  // ✅ Свернуть выпадающий список после выбора
    dropdown.classList.remove('active');
    toggleBtn.setAttribute('aria-expanded', 'false');
});
