from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView

from lomabard_lbk import settings
from webapp.models import Slider, ServiceIcon, Product, FinancialStatement, City
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
    services = ServiceIcon.objects.all()

    context = {
        'services': services,
    }
    return render(request, 'webapp/about.html', context=context)


def about_info_docs(request):
    """
    Страница О нас Документы
    """
    services = ServiceIcon.objects.all()
    reports = FinancialStatement.objects.order_by('-year')

    context = {
        'services': services,
        'reports': reports,
    }

    return render(request, 'webapp/about_docs.html', context=context)


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

def news(request):
    """
    Страница новости
    """
    return render(request, 'webapp/action.html')

def zaim(request):
    """
    Страница новости
    """
    return render(request, 'webapp/zaim.html')


def contacts(request):
    """
    Страница Контактов
    """
    cities = City.objects.prefetch_related('addresses').all()

    context = {
        'cities': cities,
    }

    return render(request, 'webapp/contacts.html', context=context)


def city_detail_view(request, slug):
    """
    Страница адреса города
    """
    city = get_object_or_404(City, slug=slug)
    addresses = city.addresses.all()  # assuming related_name='addresses'

    context = {
        'city': city,
        'addresses': addresses,
    }

    return render(request, 'webapp/adress_single.html', context=context)


def custom_404_view(request, exception):
    return render(request, 'webapp/404.html', status=404)


@csrf_exempt
def callback_request(request):
    print('--- callback_request called ---')

    if request.method != 'POST':
        print(f'Invalid method: {request.method}')
        return JsonResponse({'success': False, 'error': 'Только POST запросы'}, status=405)

    name = request.POST.get('name', '').strip()
    phone = request.POST.get('phone', '').strip()
    description = request.POST.get('description', '').strip()
    product_name = request.POST.get('product_name', '').strip()
    photo = request.FILES.get('photo')

    print(f'Received data - name: "{name}", phone: "{phone}", product_name: "{product_name}", description: "{description}", photo: {"yes" if photo else "no"}')

    if not name or not phone:
        print('Validation failed: name or phone is empty')
        return JsonResponse({'success': False, 'error': 'Имя и телефон обязательны.'})

    message_text = (
        f"<b>Новая заявка на обратный звонок</b>\n"
        f"<b>Продукт:</b> {product_name if product_name else 'Не указан'}\n"
        f"<b>Имя:</b> {name}\n"
        f"<b>Телефон:</b> {phone}\n"
        f"<b>Описание:</b> {description if description else 'Отсутствует'}"
    )

    print('Prepared message_text:')
    print(message_text)

    bot_token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    telegram_api_url = f"https://api.telegram.org/bot{bot_token}"

    try:
        if photo:
            print('Sending photo message to Telegram')
            files = {'photo': photo}
            data = {'chat_id': chat_id, 'caption': message_text, 'parse_mode': 'HTML'}
            response = requests.post(f"{telegram_api_url}/sendPhoto", data=data, files=files)
        else:
            print('Sending text message to Telegram')
            data = {'chat_id': chat_id, 'text': message_text, 'parse_mode': 'HTML'}
            response = requests.post(f"{telegram_api_url}/sendMessage", data=data)

        print(f'Telegram response status: {response.status_code}')
        if response.status_code == 200:
            print('Message sent successfully')
            return JsonResponse({'success': True})
        else:
            error_msg = response.json().get('description', 'Ошибка при отправке в Telegram')
            print(f'Telegram API error: {error_msg}')
            return JsonResponse({'success': False, 'error': error_msg})
    except Exception as e:
        print(f'Exception during Telegram request: {str(e)}')
        return JsonResponse({'success': False, 'error': str(e)})
