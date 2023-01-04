from django.urls import path

from .views import MenuView

app_name = 'menu'


urlpatterns = [
    path('', MenuView.as_view(), name='index'),
    path('<str:url>/', MenuView.as_view(), name='child'),
]
