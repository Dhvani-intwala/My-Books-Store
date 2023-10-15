from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import WishList
from django.contrib import messages

# Create your views here.


def wishlist(request):
    """ A view that provides the wishlist of products """

    return render(request, 'wishlist/wishlist.html')


# def Add_to_wishlist(request, product_id):
#     """ A view that provides a form for creating a new entry in
#     WishlistLine """

#     product = get_object_or_404(Product, pk=product_id)

#     context = {
#         'product': product,
#     }

#     if not request.user.is_authenticated:
#         messages.error(
#             request, "You must be logged in to add items to your wishlist.")
#         return redirect('login')
#     else:
#         # Create a new entry in the user's wishlist for the product
#         wishlist_item = WishList(user=request.user, product=product)
#         wishlist_item.save()
#         messages.success(
#             request, f"{product.name} has been added to your wishlist.")

#     return redirect('wishlist') 
