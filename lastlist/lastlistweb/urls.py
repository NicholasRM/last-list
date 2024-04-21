from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="Sign In"),
    path("signup/", views.signup, name="Sign Up"),
    path("lists/", views.list_view, name="My Lists"),
    path("lists/<int:list_id>/", views.inspect_list, name="A List"),
    path("lists/create/name=<str:name>/", views.create_list, name="Make new list"),
    path("lists/delete/<int:list_id>/", views.delete_list, name="Delete list"),
    path('lists/<int:list_id>/add/<int:item_id>/', views.add_list_item, name="Add list item"),
    path("lists/<int:list_id>/remove/<int:item_id>/", views.remove_list_item, name="Remove list item"), 
    path("items/", views.item_search, name="Find Products"),
    path("items/<int:item_id>/", views.item_view, name="Some Product"),
    path("vendors/", views.vendor_search, name="Find Stores"),
    path("vendors/<int:vendor_id>", views.vendor_view, name="Here's a vendor"),
]
