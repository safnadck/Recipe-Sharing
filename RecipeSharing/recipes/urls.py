from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>/', views.recipe_details, name='recipe_details'),
    path('categories/', views.category_list, name='category_list'),
    path('contact/', views.contact, name='contact'),
]
