document.querySelectorAll('.sub-dropdown-toggle').forEach(button => {
  button.addEventListener('click', function() {
    const submenu = this.closest('.sub-dropdown-section').querySelector('.sub-dropdown-list');
    if (!submenu) return;

    const isExpanded = this.getAttribute('aria-expanded') === 'true';
    this.setAttribute('aria-expanded', String(!isExpanded));
    if (isExpanded) {
      submenu.style.display = 'none';
    } else {
      submenu.style.display = 'block';
    }
  });
});
