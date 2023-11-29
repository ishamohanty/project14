"""
URL configuration for project14 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('card/',card,name='card'),

    path('carousel/',carousel,name='carousel'),

    path('collapse/',collapse,name='collapse'),

    path('dropdowns/',dropdowns,name='dropdowns'),

    path('forms/',forms,name='forms'),

    path('inputgroup/',inputgroup,name='inputgroup'),

    path('jumbtron/',jumbtron,name='jumbtron'),

    path('Listgroup/',Listgroup,name='Listgroup'),


    path('Mediaobject/',Mediaobject,name='Mediaobject'),

    path('Modal/',Modal,name='Modal'),

    path('Navs/',Navs,name='Navs'),

    path('Navbar/',Navbar,name='Navbar'),

    path('pagination/',pagination,name='pagination'),

    path('popovers/',popovers,name='popovers'),

    path('progress/',progress,name='progress'),

    path('scrollspy/',scrollspy,name='scrollspy'),

    path('spinners/',spinners,name='spinners'),

    path('toasts/',toasts,name='toasts'),

    path('tooltips/',tooltips,name='tooltips'),





    

    
]
