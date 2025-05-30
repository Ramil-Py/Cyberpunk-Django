from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about),
    path('<int:id>', views.post)
]