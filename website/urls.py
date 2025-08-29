from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="homepage"),
    path('category/<id>', views.category_display, name="category"),
    path('add_to_cart/<id>', views.add_to_cart, name = "add_to_cart"),
    path('cart', views.cart, name="cart"),
    path('delete_cart_item/<id>', views.delete_cart_item, name="delete_cart_item"),
    path('product_info/<id>', views.item_info, name="item_info"),
    path('quantity', views.quantity, name="quantity"),
    path('shop', views.shop_display, name="shop"),
    path('search/<slug:productname>', views.search, name="search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


