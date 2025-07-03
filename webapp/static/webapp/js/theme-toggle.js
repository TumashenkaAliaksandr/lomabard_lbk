document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');
    const body = document.body;

    // При загрузке восстанавливаем тему из localStorage
    if (localStorage.getItem('theme') === 'light') {
        body.classList.add('light-theme');
        themeIcon.classList.replace('bi-moon-fill', 'bi-sun-fill');
    }

    // Обработчик клика по кнопке переключения темы
    toggleBtn.addEventListener('click', () => {
        body.classList.toggle('light-theme');

        if (body.classList.contains('light-theme')) {
            // Если включена светлая тема
            themeIcon.classList.replace('bi-moon-fill', 'bi-sun-fill');
            localStorage.setItem('theme', 'light');
        } else {
            // Если возвращаемся к темной теме
            themeIcon.classList.replace('bi-sun-fill', 'bi-moon-fill');
            localStorage.setItem('theme', 'dark');
        }
    });
});
