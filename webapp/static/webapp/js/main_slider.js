document.addEventListener('DOMContentLoaded', () => {
  // Основной слайдер (ваш существующий)
  const slidesCount = document.querySelectorAll('.hero-slider input[type="radio"]').length;
  let currentSlide = 1;
  const intervalTime = 5000; // 5 секунд

  setInterval(() => {
    currentSlide++;
    if (currentSlide > slidesCount) {
      currentSlide = 1;
    }
    const radio = document.getElementById(`slide${currentSlide}`);
    if (radio) {
      radio.checked = true;
    }
  }, intervalTime);

  // Новый слайдер-коллаж - рандомное переключение
  const collageSlidesCount = document.querySelectorAll('.collage-slider input[type="radio"]').length;

  setInterval(() => {
    const randomSlide = Math.floor(Math.random() * collageSlidesCount) + 1;
    const collageRadio = document.getElementById(`collage-slide${randomSlide}`);
    if (collageRadio) {
      collageRadio.checked = true;
    }
  }, 4000); // переключаем каждые 4 секунды
});
