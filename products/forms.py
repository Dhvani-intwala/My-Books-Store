import datetime
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
    
    category = forms.ChoiceField()
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
    year = forms.IntegerField(min_value=0,
                              max_value=datetime.datetime.now().year)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'category': 'Category',
            'name': 'Name',
            'sku': 'Sku',
            'books_type': 'Books type',
            'auth_name': 'Auth name',
            'description': 'Description',
            'year': 'Year',
            'price': 'price',
            'rating': 'Rating',
            'stock': 'Stock',
            
        }

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field in self.fields:
            if field != 'country' and field != 'category'\
                 and field != 'is_deluxe' and field != 'image':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = ('border-black '
                                                            'rounded-0 '
                                                            'contact-form-input')
                self.fields[field].label = False