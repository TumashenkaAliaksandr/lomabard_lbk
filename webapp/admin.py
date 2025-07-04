from django.contrib import admin
from django.utils.html import format_html

from .models import Slider, ServiceIcon, ProductPhoto, Product, ProductFlag


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'subtitle')


@admin.register(ServiceIcon)
class ServiceIconAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview', 'link')  # столбцы в списке объектов
    search_fields = ('name',)                         # поиск по названию
    list_display_links = ('name',)                    # по чему можно кликнуть для редактирования
    readonly_fields = ('icon_preview',)               # поле только для просмотра

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="height:40px;"/>', obj.icon.url)
        return "-"
    icon_preview.short_description = 'Иконка'


class ProductPhotoInline(admin.TabularInline):
    model = ProductPhoto
    extra = 1
    fields = ('image', 'is_main')
    can_delete = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'phone', 'get_flags', 'main_photo_tag')
    search_fields = ('name', 'description', 'characteristics')
    list_filter = ('flags',)
    inlines = [ProductPhotoInline]

    def get_flags(self, obj):
        return ", ".join(flag.name for flag in obj.flags.all())
    get_flags.short_description = "Флаги"

    def main_photo_tag(self, obj):
        url = obj.main_photo()
        if url:
            return format_html('<img src="{}" style="height:50px; border-radius: 4px;" />', url)
        return "-"
    main_photo_tag.short_description = "Главное фото"
    main_photo_tag.allow_tags = True  # В новых версиях Django не обязателен, но можно оставить


@admin.register(ProductFlag)
class ProductFlagAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
