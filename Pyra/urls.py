from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('aboutus/',views.aboutUs),
    path('services/',views.services),
    path('service/<courseid>/',views.service),   # Dynamic URL
]
