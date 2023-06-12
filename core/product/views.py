from django.shortcuts import render
from .models import Product, ProductImage

def list_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "list.html", context)

