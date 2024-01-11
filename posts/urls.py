from . import views
from django.urls import path


urlpattern = [
    path('homePage/', views.homePage, name='posts_home'),
]