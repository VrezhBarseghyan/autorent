from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CarCreationForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('added_by',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model'].queryset = CarModel.objects.none()

        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['model'].queryset = CarModel.objects.filter(brand_id=brand_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['model'].queryset = self.instance.brand.model_set.order_by('name')

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = CarPost
        exclude = ('creation_date', 'update_date', 'added_by', 'car',)

class DateInput(forms.DateInput):
    input_type = 'date'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        widgets = {'date' : DateInput()}
        exclude = ('chosen_car', )