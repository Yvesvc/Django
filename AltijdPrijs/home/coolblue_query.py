import requests
from bs4 import BeautifulSoup

def get_list_coolblue(query):
    query = query.replace(' ', '+') #in de url wordt weergeven zoals bv https://www.coolblue.be/nl/games/shooter-games?redirected=call+of+duty
    url = 'https://www.coolblue.be/nl/zoeken?query=' + query
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    list_coolblue = []
    product_title = soup.find_all(class_='product__title') #finds the elements with the titles in
    product_price = soup.find_all(class_='sales-price__current') #finds the elements with the prices in
    product_image = soup.find_all(class_='product__image') #finds the elements with the images in
    product_link = soup.find_all(class_='product__title') #finds the elements with the links in
    if len(product_title) > 2:
        for i in range(3):
            dic = {}
            dic['title'] = product_title[i]['title']
            dic['price'] = float(product_price[i].get_text().replace('-', '00').replace(',', '.')) #because round prices shown as eg 113,- and , cannot be converted to float
            dic['image'] = product_image[i]['src']
            dic['link'] = 'https://coolblue.be/' + product_link[i]['href'] #because for some reason eg nl/games/shooter-games?redirected=call+of+duty is returned
            list_coolblue.append(dic)
    elif len(product_title) > 0 and len(product_title) < 3:
        for i in range(len(product_title)):
            dic = {}
            dic['title'] = product_title[i]['title']
            dic['price'] = float(product_price[i].get_text().replace('-', '00').replace(',', '.'))
            dic['image'] = product_image[i]['src']
            dic['link'] = 'https://coolblue.be/' + product_link[i]['href']
            list_coolblue.append(dic)
    return(list_coolblue)
