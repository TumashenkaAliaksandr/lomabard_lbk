document.addEventListener('DOMContentLoaded', function() {
  const MOBILE_BREAKPOINT = 768;

  function isMobile() {
    return window.innerWidth <= MOBILE_BREAKPOINT;
  }

  document.querySelectorAll('.nav-item.dropdown > a.nav-link.dropdown-toggle').forEach(link => {
    link.addEventListener('click', function(event) {
      if (!isMobile()) return;  // Для десктопа — переход стандартный

      // На мобильных — если подменю есть, блокируем переход и открываем меню вручную
      const nextMenu = this.nextElementSibling;
      if (nextMenu && nextMenu.classList.contains('dropdown-menu')) {
        event.preventDefault();

        // Используем bootstrap метод для переключения
        const bsDropdown = bootstrap.Dropdown.getOrCreateInstance(this);
        bsDropdown.toggle();
      }
    });
  });
});
