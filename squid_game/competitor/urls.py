from django.urls import path

from . import views

urlpatterns = [
    path('', views.statistics),
    path('hello/', views.hello_world),
    path('about/', views.about),
    path('prize/', views.prize),
    path('statistics/', views.statistics),
    path('player/<int:player_number>', views.player_details, name='player')
]