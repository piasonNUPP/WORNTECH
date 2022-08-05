from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('requestService', views.requestService, name = "requestService"),
    path('services', views.services, name = "services"),
    path('about', views.about, name = "about"),
    path('news', views.news, name = "news"),
    path('elements', views.elements, name = "elements"),
    path('admin1', views.admin1, name = "admin1"),
    
    path('register', views.register, name = "register"),
    path('login', views.login, name = "login"),
    path('logout', views.logout, name = "logout")
]
