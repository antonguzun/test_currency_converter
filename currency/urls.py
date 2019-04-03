from django.urls import path

from . import views

app_name = 'currency'
urlpatterns = [
    # ex: /currency/
    path('', views.index, name='index'),
    # ex: /currency/2/
    path('<int:currency_data>/', views.detail, name='detail'),
    path('convert/', views.convert, name='convert'),

]
