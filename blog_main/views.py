from django.shortcuts import render
from blogs.models import Category, Blogs
from about.models import About

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
    return render (request, 'register.html')



