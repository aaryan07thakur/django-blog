from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from blogs.models import Blogs,Category, Comment
from django.db.models import Q


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



def blogs(request, slug):
    single_blog = get_object_or_404(Blogs, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect( request.path_info) #jun page bata aako hun x taie page ma pathaie in xu

    #comments
    comments = Comment.objects.filter(blog= single_blog)
    comment_count = comments.count()
    context = {
        'single_blog' : single_blog,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'blogs.html', context)



def search(request):
    keyword = request.GET.get('keyword')

    blogs = Blogs.objects.filter(Q(title__icontains=keyword,) | Q(short_description__icontains=keyword) |Q(blog_body__icontains=keyword), status="Published")

    context= {
        'blogs': blogs,
        'keyword' : keyword,
    }
    return render (request, 'search.html', context)