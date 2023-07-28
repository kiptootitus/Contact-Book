from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name ='home'),
	path('login/', views.Login, name ='login'),
	path('register/', views.register, name ='register'),

]
