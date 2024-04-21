from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as signin, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import List, Contains, Item, Vendor, Stock
from datetime import datetime

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            signin(request, user)
            messages.success(request, f"Welcome, {user.get_username()}")
            return redirect('list_view')
        else:
            messages.success(request, "Failed to log in, please try again")
            return redirect("login")
    else:
        return render(request, "lastlistweb/login/index.html")


def list_view(request):
    lists = List.objects.filter(user_id=request.user.id)
    return render(request, "lastlistweb/list-view/index.html", {'lists':lists})


def inspect_list(request, list_id):
    lists = List.objects.get(user_id=request.user.id, list_id=list_id)
    if not lists:
        pass
        # Invalid access, redirect to user list view, display a message
    items = Contains.objects.get(list_id=list_id)
    return render(request, "lastlistweb/inspect-list/index.html", {'items':items})

def item_search(request):
    if request.method == 'POST':
        prod_name = request.POST['prod_name']
        items = Item.objects.filter(product__name__icontains=prod_name)
        return render(request, "lastlistweb/item-search/index.html", {"items":items})
        
    return render(request, "lastlistweb/item-search/index.html")

def item_view(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, "lastlistweb/item-view/index.html", {'item':item})


def vendor_search(request):
    if request.method == 'POST':
        vend_name = request.POST['vend_name']
        vendors = Vendor.objects.filter(name__icontains=vend_name)
        return render(request, "lastlistweb/vendor-search/index.html", {"vendors":vendors})
    return render(request, "lastlistweb/vendor-search/index.html")


def vendor_view(request, vendor_id):
    vendor = Vendor.objects.get(pk=vendor_id)
    inventory = Stock.objects.filter(vendor=vendor_id)
    return render(request, "lastlistweb/vendor-view/index.html", {'vendor': vendor, 'inventory': inventory})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Welcome to Last List, {user.get_username()}")
            return redirect('list_view')
    else:
        form = SignUpForm()
        return HttpResponse("<html><body><h1>Change me</h1></body></html>")
    
    return HttpResponse("<html><body><h1>Change me</h1></body></html>")

def signout(request):
    logout(request)
    redirect('login')

def add_list_item(request, list_id, item_id):
    lists = List.objects.filter(user_id=request.user.id, list_id=list_id)
    if not lists:
        return redirect('list_view')
    entry = Contains.objects.create(list=list_id, item=item_id, is_replacement=0)
    entry.save()
    return redirect('list_view')

def remove_list_item(request, list_id, item_id):
    lists = List.objects.filter(user_id=request.user.id, list_id=list_id)
    if not lists:
        return redirect('list_view')
    Contains.objects.get(list=list_id, item=item_id).delete()
    return redirect('list_view')

def create_list(request, name):
    l = List.objects.create(user=request.user.id, date_created=datetime.now().date(), name=name)
    l.save()
    return redirect('list_view')

def delete_list(request, list_id):
    l = List.objects.get(user=request.user.id, list=list_id)
    if l is not None:
        redirect('list_view')
    l.delete()
    return redirect('list_view')
    