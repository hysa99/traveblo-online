from django import forms
from .models import  Item
from django.forms.widgets import CheckboxInput, DateInput
from django.forms.widgets import DateInput
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt




INPUT_CLASSES = "py-4 px-8 rounded-2xl border"
INPUT_CLASSES_1 = "w-32 py-4 px-8 rounded-2xl border flex inline-block"
CHECKBOX_CLASSES = "w-32 py-4 px-8 rounded-2xl border flex inline-block bg-green-500"
DATE_CLASS = "date date-picker input-group date input-group-append display-inline flex justify-center bg-green-400 rounded-xl font-bold text-white"
IMAGE_CLASS = "display-inline bg-green-500 text-white font-bold rounded-2xl border no-border"



class PoolBooleanWidget(CheckboxInput):
    input_type = 'checkbox'
    attrs = {'class': INPUT_CLASSES_1}

class FoodBooleanWidget(CheckboxInput):
    input_type = 'checkbox'
    attrs = {'class': CHECKBOX_CLASSES}

class ParkingBooleanWidget(CheckboxInput):
    input_type = 'checkbox'




class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'persons', 'bedrooms', 'bathrooms', 'destinations', 'food', 'parking', 'places', 'restaurants', 'vacations', 'activities', 'trip', 'start_date', 'end_date', 'images')
        widgets = {
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'description': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'start_date': DateInput(attrs={
                'type': 'date',
                'class': DATE_CLASS,
                'id': 'datetimepicker1',
                'data-target': '#datetimepicker1',
                'date': 'dd/mm/yyyy'
            }),
            'end_date': DateInput(attrs={
                'type': 'date',
                'class': DATE_CLASS
            }),
            'pool': PoolBooleanWidget(),
            'places': FoodBooleanWidget(),
            'restaurants': FoodBooleanWidget(),
            'vacations': FoodBooleanWidget(),
            'activities': FoodBooleanWidget(),
            'trip': FoodBooleanWidget(),
            'food': FoodBooleanWidget(),
            'parking': ParkingBooleanWidget(),
            'bedrooms': forms.TextInput(attrs={
            'class': INPUT_CLASSES_1
            }),
            'bathrooms': forms.TextInput(attrs={
            'class': INPUT_CLASSES_1
            }),
            'persons': forms.TextInput(attrs={
            'class': INPUT_CLASSES_1
            }),
            'destinations': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'images': forms.FileInput(attrs={
                'multiple': False,              # Allow multiple file selection (if desired)
                'class': IMAGE_CLASS
            })
        }




CHECKBOX_CLASSES = "w-32 py-4 px-8 rounded-2xl border flex inline-block bg-green-500"



class PoolBooleanWidget(CheckboxInput):
    input_type = 'checkbox'
    attrs = {'class': INPUT_CLASSES_1}

class FoodBooleanWidget(CheckboxInput):
    input_type = 'checkbox'
    attrs = {'class': CHECKBOX_CLASSES}

class ParkingBooleanWidget(CheckboxInput):
    input_type = 'checkbox'





class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'persons', 'bedrooms', 'bathrooms', 'destinations', 'food', 'parking', 'places', 'restaurants', 'vacations', 'activities', 'trip', 'start_date', 'end_date', 'images')
        widgets = {
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'description': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'start_date': DateInput(attrs={
                'type': 'date',
                'class': DATE_CLASS,
                'id': 'datetimepicker1',
                'data-target': '#datetimepicker1',
                'date': 'dd/mm/yyyy'
            }),
            'end_date': DateInput(attrs={
                'type': 'date',
                'class': DATE_CLASS
            }),
            'pool': PoolBooleanWidget(),
            'places': FoodBooleanWidget(),
            'restaurants': FoodBooleanWidget(),
            'vacations': FoodBooleanWidget(),
            'activities': FoodBooleanWidget(),
            'trip': FoodBooleanWidget(),
            'food': FoodBooleanWidget(),
            'parking': ParkingBooleanWidget(),
            'bedrooms': forms.TextInput(attrs={
            'class': INPUT_CLASSES_1
            }),
            'bathrooms': forms.TextInput(attrs={
            'class': INPUT_CLASSES_1
            }),
            'persons': forms.TextInput(attrs={
            'class': INPUT_CLASSES_1
            }),
            'destinations': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'images': forms.FileInput(attrs={
                'multiple': False,              # Allow multiple file selection (if desired)
                'class': IMAGE_CLASS
            })
        }