from django.db import models

class Slider(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    subtitle = models.TextField("Подзаголовок", blank=True)
    button_text = models.CharField("Текст кнопки", max_length=100, blank=True)
    button_link = models.URLField("Ссылка кнопки", blank=True)
    image = models.ImageField("Изображение слайда", upload_to='slider_images/', blank=True, null=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"

    def __str__(self):
        return self.title


class ServiceIcon(models.Model):
    name = models.CharField("Название услуги", max_length=100)
    icon = models.ImageField("Иконка услуги", upload_to='service_icons/')
    link = models.URLField("Ссылка на страницу услуги", blank=True)

    class Meta:
        verbose_name = "Иконка услуги"
        verbose_name_plural = "Иконки услуг"

    def __str__(self):
        return self.name
