document.addEventListener('DOMContentLoaded', () => {
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
});
