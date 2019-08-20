from django.urls import path
# from test1.views import my_home, my_contact, my_index
from . import views


urlpatterns = [
    path('contact/', views.my_contact, name='my-contact'),
    path('index/', views.my_index, name='my-index'),
    path('', views.my_home, name='my-home'),
]