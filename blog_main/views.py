from django.shortcuts import render
from blogs.models import Category, Blogs

def home(request):
    
    featured_posts = Blogs.objects.filter(is_featured = True, status='Published' ).order_by('updated_at')
    posts= Blogs.objects.filter(is_featured = False, status='Published')
    print(posts)
    context= {
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'home.html',context)




