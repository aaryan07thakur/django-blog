from django.shortcuts import render
from blogs.models import *

# Create your views here.


def dashboard(request):
    category_count= Category.objects.all().count()
    blogs_count = Blogs.objects.all().count()
    context ={
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboard/dashboard.html', context= context)