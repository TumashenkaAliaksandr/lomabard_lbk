from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


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



class Product(models.Model):
    name = models.CharField("Название", max_length=255)
    slug = models.SlugField("Слаг", max_length=255, unique=True, default='default')
    description = models.TextField("Описание", blank=True)
    price = models.DecimalField("Цена", max_digits=12, decimal_places=2)
    characteristics = models.TextField("Характеристики", blank=True)
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Телефон',
        help_text='Телефон для связи с продавцом или службой поддержки',
        validators=[
            RegexValidator(
                regex=r'^\+?[\d\s\-\(\)]{9,20}$',
                message="Телефон должен быть в формате: '+999999999'. До 15 цифр."
            ),
        ],
    )

    # Булевы поля вместо ManyToMany flags
    is_main = models.BooleanField('На главную', default=False, blank=True)
    is_precious_metals = models.BooleanField('Драгоценные металлы', default=False, blank=True)
    is_home_appliances = models.BooleanField('Бытовая техника', default=False, blank=True)
    is_electronics = models.BooleanField('Электроника', default=False, blank=True)
    is_tools = models.BooleanField('Инструменты', default=False, blank=True)
    is_sport_tourism = models.BooleanField('Спорт/Туризм', default=False, blank=True)
    is_children = models.BooleanField('Детское', default=False, blank=True)
    is_laptops = models.BooleanField('Ноутбуки', default=False, blank=True)
    is_watches = models.BooleanField('Часы', default=False, blank=True)
    is_tv = models.BooleanField('Телевизоры', default=False, blank=True)
    is_other = models.BooleanField('Другое', default=False, blank=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['name']

    def __str__(self):
        return self.name

    def main_photo(self):
        """Возвращает URL главного фото продукта, если есть"""
        main_photo = self.photos.filter(is_main=True).first()
        if main_photo:
            return main_photo.image.url
        return None

    def get_absolute_url(self):
        """Возвращает URL детальной страницы продукта"""
        return reverse('product_detail', kwargs={'slug': self.slug})



class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField("Фото", upload_to='products/photos/')
    is_main = models.BooleanField("Главное фото", default=False)

    class Meta:
        verbose_name = "Фото продукта"
        verbose_name_plural = "Фото продуктов"

    def save(self, *args, **kwargs):
        if self.is_main:
            # Снимаем флаг главного фото с других фото этого продукта
            ProductPhoto.objects.filter(product=self.product, is_main=True).exclude(pk=self.pk).update(is_main=False)
        super().save(*args, **kwargs)

    def __str__(self):
        status = 'главное' if self.is_main else 'дополнительное'
        return f"Фото для {self.product.name} ({status})"
