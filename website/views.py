from django.shortcuts import render, redirect
from . models import Category, Products, OrderItem
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse

# Create your views here.
def home(request):
    categories = Category.objects.all()
    if request.POST:
        productname = request.POST['product_search']
        return redirect("search", productname=productname)
    
    products = Products.objects.all()
    data = {
        'categories':categories,
        'products':products,
    }
    return render(request, 'homepage.html', data)





def category_display(request, id):
    categories = Category.objects.all()
    if request.POST:
        productname = request.POST['product_search']
        return redirect("search", productname=productname)
    
    category = Category.objects.get(id=id)
    products = Products.objects.filter(category=category)
    data = {
        'categories':categories,
        'products':products,
        'category':category
    }
    return render(request, 'category.html', data)








def shop_display(request):
    categories = Category.objects.all()
    if request.POST:
        productname = request.POST['product_search']
        return redirect("search", productname=productname)
    
    ear_products = Products.objects.filter(category__name="Earphones")
    head_products = Products.objects.filter(category__name="Headphones")
    speaker_products = Products.objects.filter(category__name="Speakers")
    data = {
        'categories':categories,
        'ear_products':ear_products,
        'head_products':head_products,
        'speaker_products':speaker_products,
    }
    return render(request, 'shop.html', data)

def add_to_cart(request, id):
    product_item = Products.objects.get(id=id)
    order_item = OrderItem.objects.create(product=product_item)
    order_item.save()
    return redirect(home)

def cart(request):
    categories = Category.objects.all()
    if request.POST:
        productname = request.POST['product_search']
        return redirect("search", productname=productname)
    
    order_items = OrderItem.objects.all()
    data = {
        'order_items':order_items,
        'categories':categories,
    }
    return render(request, 'cart.html', data)

def delete_cart_item(request, id):
    order_item = OrderItem.objects.get(id=id)
    order_item.delete()
    return redirect(cart)

def item_info(request, id):
    item = Products.objects.get(id=id)
    categories = Category.objects.all()
    if request.POST:
        productname = request.POST['product_search']
        return redirect("search", productname=productname)
    
    data={
        'product':item,
        'categories':categories,
    }
    return render(request, "product_info.html", data)

def search(request, productname):
    if request.POST:
        productname = request.POST['product_search']
        return redirect("search", productname=productname)
    
    categories = Category.objects.all()
    baseproducts = Products.objects.filter(name__icontains=productname)
    catproducts = Products.objects.filter(category__name__icontains=productname)

    if baseproducts.count() > 0:
        data = {
            'products': baseproducts,
            'categories':categories,
            'productname': productname,
            'productnum': baseproducts.count()
        }
    elif catproducts.count() > 0:
        data = {
            'products': catproducts,
            'categories':categories,
            'productname': productname,
            'productnum': catproducts.count()
        }
    else:
        data = {
            'categories':categories,
            'productname': productname,
            'productnum': 0
        }
        
    return render(request, 'search.html', data)


@csrf_exempt
def quantity(request):
    id = request.POST['id']
    type_val = request.POST['type']
    item = OrderItem.objects.get(product__id=int(id))
    if type_val == 'inc':
        item.quantity += 1
    else:
        item.quantity -= 1
    item.save()
    return JsonResponse({"status": "true", "quantity": item.quantity, "product_id": id})

