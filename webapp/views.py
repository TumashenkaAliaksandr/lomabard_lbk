from django.shortcuts import render

from webapp.models import Slider


def index(request):
    slides = Slider.objects.all()
    return render(request, 'webapp/index.html', {'slides': slides})
