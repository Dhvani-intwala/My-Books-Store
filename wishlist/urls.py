from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>', views.Add_to_wishlist, name='addtowishlist'),
    path('remove_from_wishlist/<int:product_id>', views.Remove_from_wishlist, name='removefromwishlist')
]
