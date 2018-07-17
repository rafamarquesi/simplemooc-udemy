"""simplemooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from courses import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    #path('(?P<pk>\d+)/', views.details, name='details'),
    path('<slug:slug>/', views.details, name='details'),
    path('<slug:slug>/inscricao/', views.enrollment, name='enrollment'),
    path('<slug:slug>/cancelar-inscricao/', views.undo_enrollment, name='undo_enrollment'),
    path('<slug:slug>/anuncios/', views.announcements, name='announcements'),
    path('<slug:slug>/anuncios/<int:pk>', views.show_announcement, name='show_announcement'),
]
