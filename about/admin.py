from django.contrib import admin
from .models import *

# Register your models here.

class AboutAdmin(admin.ModelAdmin):
    #yo function le kunai pani data add garne permision din x in admin panel. Add button desaible garna ko lagie 
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        else:
            return False
    

admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)