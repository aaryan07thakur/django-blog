from django.contrib import admin
from .models import *



class BlogAdmin(admin.ModelAdmin):  #slug auto generate gar x according to title mening 1 word - add gar x 
    prepopulated_fields = {'slug' : ('title',)} #example : this-is-title

    list_display = ('title', 'Category', 'author', 'status' ,'is_featured') # admin pannel ma table ma heading show gar x 

    #search fields
    search_fields = ('id','title', 'Category__category_name','status')

#is_featured laei editable bana ko 
    list_editable =('is_featured',)

# Register your models here.

admin.site.register(Category)
admin.site.register(Blogs, BlogAdmin)