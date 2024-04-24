from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="lastlistweb"

urlpatterns = [
    path("", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("signup/", views.signup, name="signup"),
    path("lists/", views.list_view, name="lists"),
    path("lists/<int:list_id>/", views.inspect_list, name="listid"),
    path("items/", views.item_search, name="items"),
    path("items/<int:item_id>/", views.item_view, name="itemid"),
    path("vendors/", views.vendor_search, name="vendors"),
    path("vendors/<int:vendor_id>", views.vendor_view, name="vendorid"),
    path("lists/new-list/<str:list_name>", views.add_list, name="new-list"),
    path("lists/<int:list_id>/add/<int:item_id>", views.add_list_item, name="addlistitem")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
