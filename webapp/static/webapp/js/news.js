document.addEventListener('DOMContentLoaded', () => {
  const slider = document.querySelector('.news-slider');
  const btnPrev = document.querySelector('.slider-prev');
  const btnNext = document.querySelector('.slider-next');

  const scrollAmount = 240; // ширина одного элемента + отступы
  const autoScrollInterval = 3000; // интервал автолиста — 3 секунды

  function updateButtons() {
    btnPrev.disabled = slider.scrollLeft <= 0;
    btnNext.disabled = (slider.scrollLeft + slider.clientWidth) >= slider.scrollWidth;
  }

  function autoScroll() {
    if ((slider.scrollLeft + slider.clientWidth) >= slider.scrollWidth) {
      // Вернуться в начало, если доскроллил до конца
      slider.scrollTo({left: 0, behavior: 'smooth'});
    } else {
      slider.scrollBy({left: scrollAmount, behavior: 'smooth'});
    }
  }

  btnPrev.addEventListener('click', () => {
    slider.scrollBy({left: -scrollAmount, behavior: 'smooth'});
  });

  btnNext.addEventListener('click', () => {
    slider.scrollBy({left: scrollAmount, behavior: 'smooth'});
  });

  slider.addEventListener('scroll', updateButtons);
  updateButtons();

  // Запускаем автопрокрутку слайдера
  let autoScrollTimer = setInterval(autoScroll, autoScrollInterval);

  // Опционально: остановить автопрокрутку при наведении мыши или фокусе
  slider.addEventListener('mouseenter', () => clearInterval(autoScrollTimer));
  slider.addEventListener('mouseleave', () => {
    autoScrollTimer = setInterval(autoScroll, autoScrollInterval);
  });
});
