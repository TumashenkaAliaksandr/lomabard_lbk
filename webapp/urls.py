from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import MetalsPriceProbasAPIView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('store/', views.store, name='store'),
    path('contacts/', views.contacts, name='contacts'),
    path('action/', views.action, name='action'),
    path('api/metals-price-probas/', MetalsPriceProbasAPIView.as_view(), name='metals_price_probas'),

    ]

# Добавляем маршруты для медиа-файлов в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
