from django.urls import path
from . import views

# recipes:recipes
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipe, name='detail'),
]