from django.urls import path

from . import views


urlpatterns = [
    path("", views.index),
    path("<slug:main_menu>", views.menu)
]
