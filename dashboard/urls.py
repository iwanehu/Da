from django.urls import path
from . import views

urlpatterns = [
    path('', views.crypto_index, name='crypto_index'),
    path('refresh/', views.refresh_prices, name='refresh_prices'),

]