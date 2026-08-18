from django import forms
from blogs.models import *
from django.contrib.auth.forms import UserCreationForm

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


#blog post ko lagie 
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title','Category','featured_image','short_description', 'blog_body', 'status', 'is_featured')

#user form
class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email' ,'first_name', 'last_name', 'is_active' , 'is_staff', 'is_superuser', 'groups', 'user_permissions',)












