from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Slider, ServiceIcon, Product
import requests
import datetime



class MetalsPriceProbasAPIView(APIView):
    def get(self, request):
        try:
            today = datetime.date.today()
            start_year = datetime.date(today.year, 1, 1)

            url = 'https://api.nbrb.by/bankingots/prices'
            params = {
                'startdate': start_year.strftime('%Y-%m-%d'),
                'enddate': today.strftime('%Y-%m-%d')
            }
            r = requests.get(url, params=params)
            r.raise_for_status()
            data = r.json()

            gold_prices = [item for item in data if item.get('MetalId') == 0]
            silver_prices = [item for item in data if item.get('MetalId') == 1]

            latest_gold = max(gold_prices, key=lambda x: x['Date']) if gold_prices else None
            latest_silver = max(silver_prices, key=lambda x: x['Date']) if silver_prices else None

            if not latest_gold or not latest_silver:
                return Response({
                    "success": False,
                    "error": "Нет данных по золоту или серебру"
                })

            gold_base_price = latest_gold['Value']  # per gram pure gold
            silver_base_price = latest_silver['Value']  # per gram pure silver

            # Пробы для золота и серебра
            gold_probas = [375, 500, 583, 750, 900, 916, 950, 958]
            silver_probas = [750, 800, 875, 916, 925, 960]

            # Рассчёт цены по пробам
            gold_prices_by_proba = {}
            for prob in gold_probas:
                gold_prices_by_proba[str(prob)] = round(gold_base_price * (prob / 1000), 2)

            silver_prices_by_proba = {}
            for prob in silver_probas:
                silver_prices_by_proba[str(prob)] = round(silver_base_price * (prob / 1000), 2)

            return Response({
                "success": True,
                "gold_prices": gold_prices_by_proba,
                "silver_prices": silver_prices_by_proba,
                "date": max(latest_gold['Date'], latest_silver['Date'])
            })

        except Exception as e:
            return Response({
                "success": False,
                "error": str(e)
            })

def index(request):
    """
    Главная страница сайта.
    Загружает слайды, иконки сервисов и список всех продуктов.
    """
    slides = Slider.objects.all()
    services = ServiceIcon.objects.all()
    products = Product.objects.filter(is_main=True).order_by('name')[:6]
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
