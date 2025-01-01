from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('boy/', views.home ,name='home'),
    path('sazidul/',views.home2,name='home'), # ai same vabe iccha moto onk gula link create kora possible
]
