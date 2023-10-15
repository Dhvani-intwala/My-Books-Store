from django.contrib import admin

# Register your models here.

from wishlist.models import wishList


class wishlistlineadmin(admin.ModelAdmin):
    """Class for displaying wishlist lines in admin panel"""
    list_display = (
        'user',
        'product',
    )


admin.site.register(wishList, wishlistlineadmin)