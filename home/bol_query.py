import requests
from bs4 import BeautifulSoup

def get_list_bol(query):
    query = query.replace(' ', '+')
    url = 'https://www.bol.com/nl/s/algemeen/zoekresultaten/Ntt/' + query
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    list_bol = []
    product_title = soup.find_all(class_='product-title')
    product_price = soup.find_all(class_ ='price-block__price')
    product_image = soup.find_all(class_='h-o-hidden')
    product_link = soup.find_all(class_='product-image product-image--list')
    if len(product_title) > 2:
        for i in range(3):
            dic = {}
            dic['title'] = product_title[i].get_text()
            dic['price'] = float(product_price[i].get_text().replace('\n','').replace(' ', '').replace('-', '00').replace(',', '.'))
            dic['image'] = product_image[i].img['src']
            dic['link'] = 'https://www.bol.com' + product_link[i]['href']
            list_bol.append(dic)
    elif len(product_title) > 0 and len(product_title) <3:
        for i in range(len(product_title)):
            dic = {}
            dic['title'] = product_title[i].get_text()
            dic['price'] = float(product_price[i].get_text().replace('\n','').replace(' ', '').replace('-', '00').replace(',', '.'))
            dic['image'] = product_image[i].img['src']
            dic['link'] = 'https://www.bol.com' + product_link[i]['href']
            list_bol.append(dic)
    return(list_bol)
