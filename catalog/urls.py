from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page),
    path('category/<int:pk>', views.get_category),
    path('anime/<str:name>/<int:pk>', views.get_anime),
]
