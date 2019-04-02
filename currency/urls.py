from django.urls import path

from . import views

urlpatterns = [
    # ex: /currency/
    path('', views.index, name='index'),
    # ex: /currency/2/
    path('<int:currency_data>/', views.detail, name='detail'),

]
