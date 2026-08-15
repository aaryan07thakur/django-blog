from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import *
from django.contrib.auth.decorators import login_required

from dashboards.forms import CategoryForm

# Create your views here. 

#=========================dashboard category =====================================

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
    #submmit button laie clicakable bana ko 
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context ={
        'form': form,
    }
    return render(request,'dashboard/add_category.html', context)



def edit_category(request, pk):
    category= get_object_or_404(Category, pk=pk)
    form = CategoryForm(instance=category) # jun category ma edit garin x tyo input ma taie category aau x 
    #button laie clickable banau n laie or save garna laie or category update garna laie 
    if request.method == 'POST':
        form= CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')


    context ={
        'form':form,
        'category':category,
    }
    return render(request, 'dashboard/edit_category.html', context)



def delete_category(request, pk):
    # database bata category line and delete garne
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.delete()

    return redirect('categories')

#=================================================================================================

#=================== Blog Post ====================================================================

def posts(request):
    posts= Blogs.objects.all()
    context={
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)


