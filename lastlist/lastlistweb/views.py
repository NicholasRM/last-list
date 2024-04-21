from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as signin, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import List, Contains, Item, Vendor, Stock


# Create your views here.
def login(request):
    if request.metthod == 'POST':
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
    lists = List.objects.filter(user_id=request.user.id, list_id=list_id)
    if not lists:
        pass
        # Invalid access, redirect to user list view, display a message
    items = Contains.objects.get(list_id=list_id)
    return render(request, "lastlistweb/inspect-list/index.html", {'items':items})


def item_search(request):
    return render(request, "lastlistweb/item-search/index.html")


def item_view(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, "lastlistweb/item-view/index.html", {'item':item})


def vendor_search(request):
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