from django import forms

class ProductForm(forms.Form):

	product_query = forms.CharField(label='',widget=forms.TextInput({ "placeholder": "Vind de goedkoopste prijs" }))
		#product_query = forms.CharField(label='', initial = 'Vind de goedkoopste prijs')
