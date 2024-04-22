from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import List, Contains, Item, Vendor, Stock
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('lastlistweb:signin')
    else:
        return render(request, "lastlistweb/login/index.html")


def list_view(request):
    lists = List.objects.filter(user_id=request.user.id)
    return render(request, "lastlistweb/list-view/index.html", {'lists':lists})


def inspect_list(request, list_id):
    items = Contains.objects.filter(list=list_id)
    return render(request, "lastlistweb/inspect-list/index.html", {'items':items})

def item_search(request):
    if request.method == 'POST':
        prod_name = request.POST['search']
        items = Item.objects.filter(product__name__icontains=prod_name)
        return render(request, "lastlistweb/item-search/index.html", {"items":items})
        
    return render(request, "lastlistweb/item-search/index.html")

def item_view(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, "lastlistweb/item-view/index.html", {'item':item})


def vendor_search(request):
    if request.method == 'POST':
        vend_name = request.POST['search']
        vendors = Vendor.objects.filter(name__icontains=vend_name)
        return render(request, "lastlistweb/vendor-search/index.html", {"vendors":vendors})
    return render(request, "lastlistweb/vendor-search/index.html")


def vendor_view(request, vendor_id):
    pass
    vendor = Vendor.objects.get(pk=vendor_id)
    inventory = Stock.objects.filter(vendor=vendor_id)
    return render(request, "lastlistweb/vendor-view/index.html", {'vendor': vendor, 'inventory': inventory})

def signout(request):
    logout(request)
    return redirect("lastlistweb:signin")