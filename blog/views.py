from django.shortcuts import render
from .models import Portfolio, ExtraGallery, Service

def index(request):
    portfolio_items = Portfolio.objects.all().order_by('-created_at')
    extragallery_items = ExtraGallery.objects.all().order_by('-created_at')
    services_items = Service.objects.all().order_by('-created_at')  

    return render(request, 'blog/index.html', {
        'portfolio_items': portfolio_items,
        'extragallery_items': extragallery_items,
        'services_items': services_items,  
    })
