from webapp.models import Product, City


def products_processor(request):
    products = Product.objects.all().order_by('name')
    cities = City.objects.order_by('name')
    return {
        'products': products,
        'cities_for_menu': cities,
    }