from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(request):
    html = "<html><body>Login</body></html>"
    return HttpResponse(html)


def list_view(request):
    html = "<html><body>List View</body></html>"
    return HttpResponse(html)


def inspect_list(request, list_id):
    html = "<html><body>Inspecting List...</body></html>"
    return HttpResponse(html)


def item_search(request):
    html = "<html><body>Item Search...</body></html>"
    return HttpResponse(html)


def item_view(request, item_id):
    html = "<html><body>Item View</body></html>"
    return HttpResponse(html)


def vendor_search(request):
    html = "<html><body>Vendor Search...</body></html>"
    return HttpResponse(html)


def vendor_view(request, vendor_id):
    html = "<html><body>Vendor View</body></html>"
    return HttpResponse(html)
