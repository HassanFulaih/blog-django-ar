"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
from sellingportal.views import my_index, student, register, student_degree, my_home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', my_home, name='home'),
    url(r'^index/$', my_index, name='index'),
    url(r'^register/$', register, name='register'),
    url(r'^student/$', student, name='student'),
    url(r'^degree/(?P<st_id>[0-9]+)/', student_degree, name='degree'),
]
