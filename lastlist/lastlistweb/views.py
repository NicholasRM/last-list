from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request, "lastlistweb/login/index.html")


def list_view(request):
    return render(request, "lastlistweb/list-view/index.html")


def inspect_list(request, list_id):
    return render(request, "lastlistweb/inspect-list/index.html")


def item_search(request):
    return render(request, "lastlistweb/item-search/index.html")


def item_view(request, item_id):
    return render(request, "lastlistweb/item-view/index.html")


def vendor_search(request):
    return render(request, "lastlistweb/vendor-search/index.html")


def vendor_view(request, vendor_id):
    return render(request, "lastlistweb/vendor-view/index.html")
