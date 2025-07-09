document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('.tab-button');
  const contents = document.querySelectorAll('.tab-content');

  buttons.forEach(button => {
    button.addEventListener('click', () => {
      const tab = button.dataset.tab;

      // Снимаем активность со всех кнопок и блоков
      buttons.forEach(btn => btn.classList.remove('active'));
      contents.forEach(content => content.classList.remove('active'));

      // Активируем выбранные
      button.classList.add('active');
      document.getElementById(tab).classList.add('active');
    });
  });
});
