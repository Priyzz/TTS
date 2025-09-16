from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Product
from django.shortcuts import render, redirect, get_object_or_404
from django import forms

# Create your views here.

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'thumbnail', 'category', 'is_featured', 'stock', 'brand', 'size', 'color']


def show_main(request):
    products = Product.objects.all()
    context = {
        "nama_aplikasi": "Tim Tarkam Shop",
        'name': 'Priyanggara Zuhaynanda Zavana',
        'class': 'PBP F',
        'products' : products,
    }

    return render(request, "main.html", context)

def show_products_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_products_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_product_json_by_id(request, id):
    try:
       data = Product.objects.get(pk=id)
       json_data = serializers.serialize("json", [data])
       return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_product_xml_by_id(request, id):
    try:
        data = Product.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", data)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
       return HttpResponse(status=404)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})
