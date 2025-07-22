document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('callbackFormProduct');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    if (!form.checkValidity()) {
      form.classList.add('was-validated');
      return;
    }

    const formData = new FormData(form);

    try {
      const response = await fetch('/callback/', {  // URL эндпоинта вашего backend
        method: 'POST',
        body: formData,
        headers: {
          // CSRF токен добавьте, если нужно (зависит от вашей настройки)
          //'X-CSRFToken': getCookie('csrftoken'),
        },
      });

      const result = await response.json();

      if (result.success) {
        alert('Заявка успешно отправлена!');
        form.reset();
        form.classList.remove('was-validated');
        // Закрыть модальное окно
        const modalEl = document.getElementById('callbackModalProduct');
        const modal = bootstrap.Modal.getInstance(modalEl);
        modal.hide();
      } else {
        alert('Ошибка: ' + (result.error || 'Попробуйте позже'));
      }
    } catch (err) {
      alert('Ошибка отправки. Попробуйте позже.');
    }
  });
});
