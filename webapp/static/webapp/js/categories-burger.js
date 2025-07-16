document.addEventListener('DOMContentLoaded', () => {
  const burgerBtn = document.getElementById('categoriesBurger');
  const menu = document.getElementById('categoriesMenu');

  burgerBtn.addEventListener('click', () => {
    const expanded = burgerBtn.getAttribute('aria-expanded') === 'true' || false;
    burgerBtn.setAttribute('aria-expanded', !expanded);
    menu.classList.toggle('active');
    menu.setAttribute('aria-hidden', expanded);
  });

  // Дополнительно можно закрывать меню при клике вне элементов
  document.addEventListener('click', (e) => {
    if (!menu.contains(e.target) && !burgerBtn.contains(e.target)) {
      burgerBtn.setAttribute('aria-expanded', 'false');
      menu.classList.remove('active');
      menu.setAttribute('aria-hidden', 'true');
    }
  });
});
