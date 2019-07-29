from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm
import re
import requests
from . import bol_query, ebay_query, coolblue_query, aliexpress_query, query_total_sorted


def product_url(request):
	if request.method == 'POST': #als op submit hebt geduwd
		form = ProductForm(request.POST) #populates the form with whatever the user tries to submit
		if form.is_valid():
			product_query = form.cleaned_data['product_query'] #captures the url from form
			product_query = str(product_query) #convert to string
			list_bol = bol_query.get_list_bol(product_query) #get list of dictionaries of bol
			list_ebay = ebay_query.get_list_ebay(product_query)
			list_coolblue = coolblue_query.get_list_coolblue(product_query)
			list_aliexpress = aliexpress_query.get_list_aliexpress(product_query)
			list_all_sorted = query_total_sorted.get_list_total(list_bol, list_ebay, list_coolblue, list_aliexpress)
			len_list_all_sorted = len(list_all_sorted) #Count number of results, because message in results.html if no results found
			return render(request, 'home/result2.html', {'list_all_sorted': list_all_sorted,'len_list_all_sorted': len_list_all_sorted })
	form = ProductForm() #als op pagina terechtkomt
	return render(request, 'home/home.html', {'form': form})
