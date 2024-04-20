from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="Sign In"),
    path("signup/", views.signup, name="Sign Up"),
    path("lists/", views.list_view, name="My Lists"),
    path("lists/<int:list_id>/", views.inspect_list, name="A List"),
    path("items/", views.item_search, name="Find Products"),
    path("items/<int:item_id>/", views.item_view, name="Some Product"),
    path("vendors/", views.vendor_search, name="Find Stores"),
    path("vendors/<int:vendor_id>", views.vendor_view, name="Here's a vendor"),
]
