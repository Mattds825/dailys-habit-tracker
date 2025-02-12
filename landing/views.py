from django.shortcuts import render
from .models import About

# Create your views here.

def landing_page(request):
    """
    Renders about page with the correct list of features
    """
    about = About.objects.order_by('-updated_on').first()
    features = about.features.all()
    return render(request, 'landing/landing.html', 
                  {'about': about,
                   'features': features
                   }
            )
