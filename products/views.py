from django.shortcuts import render
from .models import products




def all_products(request):
    """ A view to show all products , sorting and searching queries """

    products = products.objects . all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html' , context)




