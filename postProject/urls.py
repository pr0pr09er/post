from django.contrib import admin
from django.urls import path, include
from postApp import views

login_password = [
    path('', views.login_password)
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_password),
    path('posts', include('postApp.urls')),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('err/', views.err),
    path('access/', views.access),
    path('json/', views.json_return),
    path('set/', views.set),
    path('get/', views.get)
]
