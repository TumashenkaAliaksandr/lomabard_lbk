from webapp.models import Product


def products_processor(request):
    products = Product.objects.all().order_by('name')
    return {
        'products': products
    }