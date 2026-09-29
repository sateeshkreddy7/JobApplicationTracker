
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('add/', views.add_application, name='add_application'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:id>/', views.edit_application, name='edit_application'),
    path('delete/<int:id>/', views.delete_application, name='delete_application'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='applications/login.html'
        ),
        name='login'
    ),
    path(
    'logout/',
    auth_views.LogoutView.as_view(),
    name='logout'
),
]