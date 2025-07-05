from django.shortcuts import render, get_object_or_404

from webapp.models import Slider, ServiceIcon, Product


def index(request):
    """
    Главная страница сайта.
    Загружает слайды, иконки сервисов и список всех продуктов.
    """
    slides = Slider.objects.all()
    services = ServiceIcon.objects.all()
    products = Product.objects.all().order_by('name')
    # Не ищем конкретный продукт по слагу, т.к. это главная страница
    context = {
        'slides': slides,
        'services': services,
        'products': products,
    }
    return render(request, 'webapp/index.html', context)


def product_detail(request, slug):
    """
    Страница детального просмотра продукта.
    Получает продукт по слагу и передаёт в шаблон.
    """
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'webapp/single_product.html', {'product': product})


def about(request):
    """
    Страница О нас
    """
    return render(request, 'webapp/about.html')


def store(request):
    """
    Страница Магазина
    """
    return render(request, 'webapp/store.html')


def action(request):
    """
    Страница акций
    """
    return render(request, 'webapp/action.html')


def contacts(request):
    """
    Страница Контактов
    """
    return render(request, 'webapp/contacts.html')


def custom_404_view(request, exception):
    return render(request, 'webapp/404.html', status=404)
