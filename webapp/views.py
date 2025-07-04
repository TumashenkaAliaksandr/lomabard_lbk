from django.shortcuts import render

from webapp.models import Slider, ServiceIcon


def index(request):
    slides = Slider.objects.all()
    services = ServiceIcon.objects.all()
    return render(request, 'webapp/index.html', {'slides': slides, 'services': services})


def custom_404_view(request, exception):
    return render(request, 'webapp/404.html', status=404)
