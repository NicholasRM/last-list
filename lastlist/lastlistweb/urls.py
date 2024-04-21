from django.urls import path
from . import views

app_name="lastlistweb"

urlpatterns = [
    path("", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    #path("signup/", views.signup, name="Sign Up"),
    path("lists/", views.list_view, name="lists"),
    path("lists/<int:list_id>/", views.inspect_list, name="listid"),
    path("items/", views.item_search, name="items"),
    path("items/<int:item_id>/", views.item_view, name="itemid"),
    path("vendors/", views.vendor_search, name="vendors"),
    path("vendors/<int:vendor_id>", views.vendor_view, name="vendorid"),
]
