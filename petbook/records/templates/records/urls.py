from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    path('', views.home_view, name='home'),

    # Аутентифікація
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Панель користувача
    path('dashboard/', views.dashboard, name='dashboard'),

    # CRUD для тварин
    path('animals/add/', views.create_animal, name='create_animal'),
    path('animals/<int:id>/edit/', views.update_animal, name='update_animal'),
    path('animals/<int:id>/delete/', views.delete_animal, name='delete_animal'),

    # CRUD для лікарів
    path('doctors/', views.list_doctors, name='list_doctors'),
    path('doctors/add/', views.create_doctor, name='create_doctor'),

    # CRUD для візитів
    path('visits/', views.list_visits, name='list_visits'),
    path('visits/add/', views.create_visit, name='create_visit'),

    # Генерація PDF
    path('animals/<int:animal_id>/pdf/', views.generate_pdf, name='generate_pdf'),
]
