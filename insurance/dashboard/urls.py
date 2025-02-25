from django.contrib import admin
from django.urls import path
from dashboard import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.about, name="about"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("about/", views.about, name="about"),
    path("comparison/", views.comparison, name="comparison"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('healthins/', views.healthins, name='healthins'),
    path('autoins/', views.autoins, name='autoins'),
    path('lifeins/', views.lifeins, name='lifeins'),
    path('healthdetail/', views.healthdetail, name='healthdetail'),
    path('autodetail/', views.autodetail, name='autodetail'),
    path('lifedetail/', views.lifedetail, name='lifedetail'),

]
