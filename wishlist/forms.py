from django import forms
from .models import wishList


class SetWishlist(forms.ModelForm):
    """Form for setting product state of favourite"""

    class Meta:
        model = wishList
        fields = []