document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('addressToggleBtn');
  const dropdown = document.getElementById('addressDropdown');
  const cityBtns = document.querySelectorAll('.city-btn');
  const addressBlocks = document.querySelectorAll('.address-block');
  const mapIframe = document.querySelector('.address-map-real iframe');

  let scrollPosition = 0;

  toggleBtn.addEventListener('click', () => {
    // Сохраняем текущий скролл
    scrollPosition = window.pageYOffset || document.documentElement.scrollTop;

    const isActive = dropdown.classList.toggle('active');
    toggleBtn.setAttribute('aria-expanded', isActive);

    if (isActive && cityBtns.length) showCity(cityBtns[0]);

    // Восстанавливаем скролл страницы сразу, чтобы избежать скачка вниз
    window.scrollTo({ top: scrollPosition, behavior: 'auto' });
  });

  cityBtns.forEach(btn => {
    btn.addEventListener('click', () => showCity(btn));
  });

  function showCity(btn) {
    cityBtns.forEach(b => b.setAttribute('aria-expanded', 'false'));
    btn.setAttribute('aria-expanded', 'true');
    const city = btn.getAttribute('data-city');
    document.querySelectorAll('.city-addresses').forEach(section => {
      if (section.getAttribute('data-city-addresses') === city) {
        section.classList.add('active');
      } else {
        section.classList.remove('active');
      }
    });
  }

  addressBlocks.forEach(block => {
    block.style.cursor = 'pointer';
    block.addEventListener('click', () => {
      const coords = block.getAttribute('data-coords');
      if (!coords) return;
      const apiKey = "ВАШ_GOOGLE_MAPS_API_KEY"; // замените на ваш ключ
      const srcUrl = `https://www.google.com/maps/embed/v1/place?key=${apiKey}&q=${encodeURIComponent(coords)}`;
      mapIframe.src = srcUrl;
      addressBlocks.forEach(el => el.classList.remove('selected'));
      block.classList.add('selected');
    });
  });
});
