from django.urls import path

from . import views
# if we leave the '' empty in the path method below, it will default to this app/model. So in this case it would be root_address + /listings
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
]
