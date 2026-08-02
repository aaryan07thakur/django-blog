
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static  #django ko static function layau x eg: css,js,image file haru show django le route chaine x
                                            #tyo route banau ne helper function ho static()
from django.conf import settings        #settings.py vitra ko value use garna din x

urlpatterns = [
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category')
]