"""
URL configuration for blog_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf.urls.static import static  #django ko static function layau x eg: css,js,image file haru show django le route chaine x
                                            #tyo route banau ne helper function ho static()
from django.conf import settings        #settings.py vitra ko value use garna din x
from blogs import views as BlogsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/', include('blogs.urls')),

    #search endpoint search Url first 
    path('blogs/search/', BlogsViews.search, name= 'search' ),

    #slug url last
    path('blogs/<slug:slug>/',BlogsViews.blogs, name='blogs'),
    

    path('register/', views.register, name= 'register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    #Dashboards
    path('dashboard/', include('dashboards.urls')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  #media_url vnae ko browser le use garne URL prefix
                                                #media_root: Server ma file rakhne real folder
