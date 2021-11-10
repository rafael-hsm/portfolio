from django.urls import path

from portfolio.base.views import index

app_name = 'base'
urlpatterns = [
    path('', index, name='index'),
]
