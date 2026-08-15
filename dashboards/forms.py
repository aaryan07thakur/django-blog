from django import forms
from blogs.models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


#blog post ko lagie 
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('title','Category','featured_image','short_description', 'blog_body', 'status', 'is_featured')