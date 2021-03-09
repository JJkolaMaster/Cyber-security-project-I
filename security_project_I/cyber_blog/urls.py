from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='cyber_blog-home'),
    path('about/', views.about, name='cyber_blog-about'),
]