from django.shortcuts import render,redirect
from blogs.models import Category, Blogs
from about.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    
    featured_posts = Blogs.objects.filter(is_featured = True, status='Published' ).order_by('updated_at')
    posts= Blogs.objects.filter(is_featured = False, status='Published')

#fetch about us from backend
    try:
        about = About.objects.get() #get() le 1 ta data matrai fetch gar x
    except:
        about = None

    context= {
        'featured_posts': featured_posts,
        'posts': posts,
        'about' : about,
    }
    return render(request, 'home.html',context)






def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:

        form = RegistrationForm()
    context={
        'form': form
    }
    return render (request, 'register.html', context)



def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user= auth.authenticate(request, username= username, password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('dashboard')

    #default authentication form by django
    form = AuthenticationForm()
    context={
        'form': form,
    }
    return render(request, 'login.html', context)






def logout(request):
    auth.logout(request)
    return redirect('home')

