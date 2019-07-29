#Voorwaarde: alle list_sites moeten structuur hebben van dictionnary met keys title, price, image, urls
#Nog toevoegen voor amazon, ali

def get_list_total(list_bol, list_ebay, list_coolblue, list_aliexpress):
    total = list_bol + list_ebay + list_coolblue + list_aliexpress #concatenate list of products of different online sites
    total_sorted = sorted(total, key=lambda k: k['price']) #sort elements in list based on price
    return(total_sorted)
