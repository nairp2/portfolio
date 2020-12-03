from django.urls import path
from portfolio_app import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.portfolio_index, name='portfolio_index'),
    path('projects/<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
    path('contact/', views.contact, name='contact'),
]
