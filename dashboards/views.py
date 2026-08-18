from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import *
from django.contrib.auth.decorators import login_required, permission_required

from dashboards.forms import *
from django.template.defaultfilters import slugify  # yo django ko built-in function ho yes le normal title laie url-friendly slug ma convert gar x 
from django.contrib.auth.models import User


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



def add_post(request):
    if request.method =='POST':
         #request.files le uploaded file laie form ma pathu x and request.Post le test laie form ma pathau x 
        form = BlogPostForm(request.POST, request.FILES)

        if form.is_valid():
#yes le object banau x but database ma save hudai n. post ma temprorily save hun x. yesto garnu ko resion author form bata fix
#va ko hudai n yati bela samma, author mannualy save hun x user jun ma login hun x taie author ho vane r save hun x
            post = form.save(commit=False)   
            post.author = request.user
#post.save() database ma save hun x aba and post id generae gar x then  post.id slug banau n  kam lag x
            post.save()

            title = form.cleaned_data['title'] #title nikal x 

#title ma slug generate gar x then post id pani last am concatinate gar x unique huna ko lagie 
            post.slug = slugify(title) + '-'+str(post.id)
            post.save() # you save le database ma update gar x with unique slug 
            return redirect('posts')
    form= BlogPostForm()
    context={
        'form':form
    }
    return render (request, 'dashboard/add_post.html',context)



def edit_post(request, pk):
    #url bata aayeko primary key(pk) ko baisi ma post khoj x
    post= get_object_or_404(Blogs, pk=pk)

   #post request ho vane updated data receive garne
    if request.method == 'POST':
        #user le form bata patha ko update data existing post ma rakh x (instance=post ) ko help le
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post=form.save() #exiting post update gar x 
            title= form.cleaned_data['title'] #title line pani form bata update gar x
            #update title x vnae slug create gar x  
            post.slug= slugify(title) + '-'+str(post.id)
            post.save() #datebase ma update gar x

            return redirect('posts') #then post page ma lag x
    else:
        form = BlogPostForm(instance=post) #get request x vane existing post ko data form ma show gar x 
    context={
        'post': post,
        'form': form,
    }
    return render (request, 'dashboard/edit_post.html', context)




def delete_post(request,pk):
    post = get_object_or_404(Blogs,pk=pk)
    if request.method == 'POST':
        post.delete()

    return redirect ('posts')



#=====================Users==============================================

@permission_required('auth.view_user') #login user laie permission vayo vane matrai access garna mil x urls 
def users(request):
    users = User.objects.all()
    context={
        'users':users
    }
    return render(request, 'dashboard/users.html', context)




@permission_required('auth.add_user')
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
#render the form
    form = AddUserForm()
    context ={
        'form':form
    }
    return render (request, 'dashboard/add_user.html',context)


def edit_user(request,pk):
    user= get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form = EditUserForm(instance=user)
    context={
        'form': form
    }
    return render(request, 'dashboard/edit_user.html', context)


def delete_user(request,pk):
    #take user object
    user= get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
    return redirect('users')


