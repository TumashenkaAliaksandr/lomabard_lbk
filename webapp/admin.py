from django.contrib import admin
from django.utils.html import format_html
from django import forms
from .models import Slider, ServiceIcon, ProductPhoto, Product, FinancialStatement, Address, City, SocialNetwork, \
    Document


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


from django import forms
from django.contrib import admin
from .models import City, Address

class AddressForm(forms.ModelForm):
    phones = forms.CharField(
        label='Телефоны',
        widget=forms.Textarea(attrs={'rows': 3, 'style': 'font-family: monospace;'}),
        required=False,
        help_text='Введите каждый номер телефона с новой строки'
    )

    class Meta:
        model = Address
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Преобразуем JSON список phones в многострочный текст для отображения
        phones_data = self.instance.phones if self.instance and self.instance.phones else []
        if isinstance(phones_data, list):
            self.initial['phones'] = '\n'.join(phones_data)
        else:
            # на всякий случай, если вдруг хранится не список
            self.initial['phones'] = phones_data

    def clean_phones(self):
        data = self.cleaned_data['phones']
        # Разбиваем по строкам, фильтруем пустые
        phones_list = [line.strip() for line in data.splitlines() if line.strip()]
        return phones_list


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    form = AddressForm
    list_display = ('address', 'city', 'working_hours')
    list_filter = ('city',)
    search_fields = ('address', 'note')


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'icon')
    search_fields = ('name',)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'registration_certificate_link', 'ministry_of_finance_license_link']
    readonly_fields = []

    def registration_certificate_link(self, obj):
        if obj.registration_certificate:
            return format_html('<a href="{}" target="_blank">Просмотр</a>', obj.registration_certificate.url)
        return "-"
    registration_certificate_link.short_description = "Свидетельство о регистрации"

    def ministry_of_finance_license_link(self, obj):
        if obj.ministry_of_finance_license:
            return format_html('<a href="{}" target="_blank">Просмотр</a>', obj.ministry_of_finance_license.url)
        return "-"
    ministry_of_finance_license_link.short_description = "Лицензия мин. финансов"
