from django import forms
from OrderUp.models import Resturant, Order
from django.forms.widgets import FileInput
from django.forms import ModelForm, FileInput
from PIL import Image
MAX_UPLOAD_SIZE = 2500000

class ResturantForm(forms.ModelForm):
    name   = forms.CharField(max_length = 20)
    image = forms.FileField(widget=forms.FileInput)


    category  = forms.CharField(max_length = 20)
    phone  = forms.CharField(max_length = 20)

    address  = forms.CharField(max_length = 20)
    menu  = forms.CharField(max_length = 20)
    price  = forms.CharField(max_length = 20)

    class Meta:
        model = Resturant
        fields=['name','image','category','phone','address','menu','price']

    def clean(self):
        cleaned_data = super(ResturantForm,self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
             super(ResturantForm, self).__init__(*args, **kwargs)
             for fieldname in self.fields:
                 self.fields[fieldname].help_text = None

class OrderForm(forms.Form):
    quantity = forms.CharField(max_length = 200)
    
    class Meta:
        model = Order
        fields=['quantity']
                             
    def clean(self):

        cleaned_data = super(OrderForm,self).clean()
        return cleaned_data

    def __init__(self, *args, **kwargs):
             super(OrderForm, self).__init__(*args, **kwargs)
             for fieldname in self.fields:
                 self.fields[fieldname].help_text = None