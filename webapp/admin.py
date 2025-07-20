from django.contrib import admin
from django.utils.html import format_html

from .models import Slider, ServiceIcon, ProductPhoto, Product, FinancialStatement


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
    list_display = (
        'name',
        'price',
        'phone',
        'flags_display',
        'main_photo_tag',
    )
    search_fields = ('name', 'description', 'characteristics')

    # Фильтровать теперь по булевым полям нужно через list_filter с перечислением полей
    list_filter = (
        'is_main',
        'is_precious_metals',
        'is_home_appliances',
        'is_electronics',
        'is_tools',
        'is_sport_tourism',
        'is_children',
        'is_laptops',
        'is_watches',
        'is_tv',
        'is_other',
    )

    inlines = [ProductPhotoInline]

    def flags_display(self, obj):
        flags = []
        if obj.is_main:
            flags.append("На главную")
        if obj.is_precious_metals:
            flags.append("Драгоценные металлы")
        if obj.is_home_appliances:
            flags.append("Бытовая техника")
        if obj.is_electronics:
            flags.append("Электроника")
        if obj.is_tools:
            flags.append("Инструменты")
        if obj.is_sport_tourism:
            flags.append("Спорт/Туризм")
        if obj.is_children:
            flags.append("Детское")
        if obj.is_laptops:
            flags.append("Ноутбуки")
        if obj.is_watches:
            flags.append("Часы")
        if obj.is_tv:
            flags.append("Телевизоры")
        if obj.is_other:
            flags.append("Другое")

        return ", ".join(flags) if flags else "-"

    flags_display.short_description = "Флаги"

    def main_photo_tag(self, obj):
        url = obj.main_photo()
        if url:
            return format_html('<img src="{}" style="height:50px; border-radius:4px;" />', url)
        return "-"

    main_photo_tag.short_description = "Главное фото"

@admin.register(FinancialStatement)
class FinancialStatementAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
    fields = (
        'name',
        'year',
        'balance_pdf',
        'notes_pdf',
        'profit_loss_pdf',
        'capital_change_pdf',
        'cash_flow_pdf',
    )
