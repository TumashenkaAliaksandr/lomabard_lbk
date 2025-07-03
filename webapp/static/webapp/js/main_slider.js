document.addEventListener('DOMContentLoaded', () => {
    const slidesCount = 3; // Количество слайдов
    let currentSlide = 1;
    const intervalTime = 5000; // Интервал переключения в миллисекундах (5 секунд)

    setInterval(() => {
        currentSlide++;
        if (currentSlide > slidesCount) {
            currentSlide = 1;
        }
        // Активируем соответствующую радио-кнопку
        const radio = document.getElementById(`slide${currentSlide}`);
        if (radio) {
            radio.checked = true;
        }
    }, intervalTime);
});
