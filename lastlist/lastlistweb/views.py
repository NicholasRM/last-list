from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import List, Contains, Item, Vendor, Stock, AuthUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.success(request, "Something went wrong signing you in...")
        return redirect('lastlistweb:signin')
    else:
        return render(request, "lastlistweb/login/index.html")


def list_view(request):
    if not request.user.is_authenticated:
        return redirect('lastlistweb:signin')
    if request.method == "POST":
        list_name = request.POST['list_name']
        return redirect("lastlistweb:new-list", list_name=list_name)
    lists = List.objects.filter(user_id=request.user.id)
    return render(request, "lastlistweb/list-view/index.html", {'lists':lists})


def inspect_list(request, list_id):
    try:
        _ = List.objects.get(user=request.user.id, list_id=list_id)
    except:
        return redirect('lastlistweb:lists')
    items = Contains.objects.filter(list=list_id)
    return render(request, "lastlistweb/inspect-list/index.html", {'items':items})

def item_search(request):
    if request.method == 'POST':
        prod_name = request.POST['search']
        items = Item.objects.filter(product__name__icontains=prod_name)
        return render(request, "lastlistweb/item-search/index.html", {"items":items})
    items = Item.objects.all()
    return render(request, "lastlistweb/item-search/index.html",{"items":items})

def item_view(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except:
        item = None
    try:
        lists = List.objects.filter(user=request.user.id)
    except:
        return redirect("lastlistweb:signin")
    return render(request, "lastlistweb/item-view/index.html", {'item':item, 'lists':lists})


def vendor_search(request):
    if request.method == 'POST':
        vend_name = request.POST['search']
        vendors = Vendor.objects.filter(name__icontains=vend_name)
        return render(request, "lastlistweb/vendor-search/index.html", {"vendors":vendors})
    vendors = Vendor.objects.all()
    return render(request, "lastlistweb/vendor-search/index.html", {"vendors":vendors})


def vendor_view(request, vendor_id):
    vendor = Vendor.objects.get(pk=vendor_id)
    inventory = Stock.objects.filter(vendor=vendor_id)
    return render(request, "lastlistweb/vendor-view/index.html", {'vendor': vendor, 'inventory': inventory})

def signout(request):
    logout(request)
    messages.success(request, "Goodbye for now")
    return redirect("lastlistweb:signin")

def add_list(request, list_name):
    from datetime import datetime
    if not request.user.is_authenticated:
        return redirect("lastlistweb:signin")
    list = List.objects.create(user=AuthUser.objects.get(id=request.user.id), name=list_name, date_created=datetime.now().date())
    list.save()
    return redirect("lastlistweb:lists")

def add_list_item(request, list_id, item_id):
    if not request.user.is_authenticated:
        return redirect("lastlistweb:signin")
    try:
        List.objects.get(user=request.user.id, list_id=list_id)
    except:
        return redirect("lastlistweb:lists")
    try:
        c = Contains.objects.get(list=list_id, item=item_id)
        messages.success(request, "This list already has that item")
        redirect("lastlistweb:itemid", item_id=item_id)
    except:
        pass
    try:
        entry = Contains.objects.create(list=List.objects.get(pk=list_id), item=Item.objects.get(pk=item_id), is_replacement=0)
    except:
        return redirect("lastlistweb:itemid", item_id=item_id)
    try:
        entry.save()
    except:
        pass
    messages.success(request, "Item successfully added to list")
    return redirect("lastlistweb:itemid", item_id=item_id)

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        if not password == confirm_password and not (password and confirm_password):
            messages.success(request, "Your passwords did not match...")
            return render(request, 'lastlistweb/signup/index.html')
        try:
            u = User.objects.get(username=username)
            messages.success(request, "That username is already taken...")
            redirect("lastlistweb:signin")
        except:
            pass
        
        try:
            u = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            u.save()
            login(request, authenticate(request, username=username, password=password))
            return redirect("lastlistweb:signin")
        except:
            return render(request, 'lastlistweb/signup/index/html')
        
    return render(request, 'lastlistweb/signup/index.html')