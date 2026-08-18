from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "categories"  #admin panel ma correct speing aau x prural ma 


    def __str__(self):
        return self.category_name


STATUS_CHOICES ={
    ("Draft", "Draft"),
    ("Published", "Published")
}






class Blogs(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models. ImageField(upload_to= 'uploads/%y/%m/%d')
    short_description = models.TextField(max_length=2000)
    blog_body = models.TextField (max_length= 3000)
    status= models.CharField( max_length=50, choices= STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)


    class Meta:
            verbose_name_plural = "Blogs"  #admin panel ma correct speing aau x prural ma 
    

    def __str__(self):
        return self.title


#comment model 
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    comment = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
            return self.comment
