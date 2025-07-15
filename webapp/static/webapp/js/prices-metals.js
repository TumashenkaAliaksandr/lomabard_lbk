document.addEventListener('DOMContentLoaded', () => {
  fetch('/api/metals-price-probas/')  // Убедитесь, что URL совпадает с вашим urls.py
    .then(resp => {
      if (!resp.ok) throw new Error('Ошибка загрузки данных');
      return resp.json();
    })
    .then(data => {
      if (!data.success) {
        console.error('Ошибка данных:', data.error);
        setDefaults();
        return;
      }

      // Обновляем цены золота по пробам
      for (const [proba, price] of Object.entries(data.gold_prices)) {
        const cell = document.querySelector(`[data-rate="gold-${proba}"]`);
        if (cell) cell.textContent = price.toFixed(2);
      }

      // Обновляем цены серебра по пробам
      for (const [proba, price] of Object.entries(data.silver_prices)) {
        const cell = document.querySelector(`[data-rate="silver-${proba}"]`);
        if (cell) cell.textContent = price.toFixed(2);
      }
    })
    .catch(err => {
      console.error('Ошибка загрузки или парсинга:', err);
      setDefaults();
    });

  function setDefaults() {
    document.querySelectorAll('[data-rate^="gold-"]').forEach(cell => cell.textContent = '-');
    document.querySelectorAll('[data-rate^="silver-"]').forEach(cell => cell.textContent = '-');
  }
});
