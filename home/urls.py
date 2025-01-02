from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('about',views.about,name='about'),
    path('project',views.projects,name='project'),
    path('contact',views.contact,name='contact'),
    path('signup',views.signup,name='signup'),
]
