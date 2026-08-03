#context_processor vane ko django ko yesto function ho jas le every template ma automatically data pathau x 
#repatedly sabai views ma same data pathau nu n paryous vane r use garin x 

from .models import Category

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories= categories)