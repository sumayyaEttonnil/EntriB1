from django.shortcuts import render
from .models import Product,Cart
from django.http import HttpResponse


def product_list(request):
    products = Product.objects.all()
    return render(request,'home/product_list.html',{'products':products})


def homepage(request):
    return HttpResponse("THIS IS A HOMEPAGE")


def cartlist(request):
    cartproducts = Cart.objects.all()
    return render(request,'home/car_list.html',{'cartproducts':cartproducts})
# Create your views here.
