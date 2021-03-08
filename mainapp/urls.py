from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.redirect_home),
    path('home/', views.home_page, name='home_page'),
    path('test-speed/', views.do_test, name='test_page'),
]
