from django import forms


class SimpleForm(forms.Form):
   departure = forms.CharField(max_length=100, label="From")
   destination = forms.CharField(max_length=100, label="To")
   date_depart = forms.DateField(input_formats=['%Y-%m-%d'])
   date_return = forms.DateField(input_formats=['%Y-%m-%d'])



