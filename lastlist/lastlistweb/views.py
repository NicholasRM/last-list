from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("Login")

def list_view(request):
    return HttpResponse("list view")

def inspect_list(request, list_id):
    return HttpResponse("inspecting list...")

def item_search(request):
    return HttpResponse("looking for items...")

def item_view(request, item_id):
    return HttpResponse("Here's an item")

def vendor_search(request):
    return HttpResponse("here's some vendors")

def vendor_view(request, vendor_id):
    return HttpResponse("Here's a vendor with some items")