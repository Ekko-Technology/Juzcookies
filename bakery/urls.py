from django.urls import path
from . import views

urlpatterns = [
    path('pastries/', views.pastries, name='pastries'),
    path('cakes/', views.cakes, name='cakes'),

]