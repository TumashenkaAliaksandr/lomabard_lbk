from django.contrib import admin
from django.utils.html import format_html

from .models import Slider, ServiceIcon


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
