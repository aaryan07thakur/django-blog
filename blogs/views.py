from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blogs.models import Blogs,Category


# Create your views here.
def posts_by_category(request, category_id):
    #fetch teh post that belongs to the category with the id category_id
    posts = Blogs.objects.filter(status='Published', Category= category_id)
    # category = Category.objects.get(pk=category_id)
    #custome 404 error pani banau n sakin x 404.html page ma setting.py ko debug ma false and ALLOWED_HOSTS ma '*' rakda hun x
    category = get_object_or_404(Category, pk = category_id)
 
    context = {
        'posts' : posts,
        'category' : category
        
    }
    return render (request, 'posts_by_category.html', context)