from django.urls import path

from .views import FormView

app_name = 'currency'
urlpatterns = [
    # ex: /currency
    path('', FormView.as_view(), name='convert'),
]
