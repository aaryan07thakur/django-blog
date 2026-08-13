from django.shortcuts import render
from blogs.models import *
from django.contrib.auth.decorators import login_required

from dashboards.forms import CategoryForm

# Create your views here.

@login_required(login_url= 'login')  #default decorators
def dashboard(request):
    category_count= Category.objects.all().count()
    blogs_count = Blogs.objects.all().count()
    context ={
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboard/dashboard.html', context= context)



def categories(request):
    return render(request, 'dashboard/categories.html' )


def add_category(request):
    form = CategoryForm()
    context ={
        'form': form,
    }
    return render(request,'dashboard/add_category.html', context)