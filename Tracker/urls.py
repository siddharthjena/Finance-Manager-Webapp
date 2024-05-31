from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.budget_view, name='dashboard'),
    path('home/', views.home_view, name= 'home'),
    path('payments/', views.payments, name= 'payments'),
]