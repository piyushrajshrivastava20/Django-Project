"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from pages.views import home_view
from products.views import teams_detail,rankig_detail,testrankig_detail , ground_detail, stat, runs,moreground,player
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
 
    # path('product/<int:my_id>/',product_detail_view,name='product'),
   
    path('team/',teams_detail,name='team'),
    path('ranking/',rankig_detail,name='ranking'),
    path('testranking/',testrankig_detail,name='testranking'),
    path('ground/',ground_detail,name='ground'),
    # path('moregrounds',ground_detail,name=ground),
    path('stat/',stat,name='stat'),
    path('stats/',runs,name='runs'),
    path('moregrounds/', moreground, name='ground1'),
     path('stat3/', player, name='player'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
