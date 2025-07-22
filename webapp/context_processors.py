from webapp.models import Product, City, SocialNetwork


def products_processor(request):
    products = Product.objects.all().order_by('name')
    cities = City.objects.order_by('name')
    social_networks = SocialNetwork.objects.all()
    return {
        'products': products,
        'cities_for_menu': cities,
        'social_networks': social_networks,
    }