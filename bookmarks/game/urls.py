from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('create/', views.game_create, name='create'),
    path('detail/<int:id>/<slug:slug>/',
         views.game_detail, name='detail'),
]