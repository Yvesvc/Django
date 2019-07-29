import requests
from bs4 import BeautifulSoup

def get_list_aliexpress(query):
    query = query.replace(' ', '+')
    url = 'https://nl.aliexpress.com/wholesale?SearchText=' + query
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    list_aliexpress = []
    product_title = soup.find_all(class_='history-item product ')
    product_price = soup.find_all(class_='value')
    product_image = soup.find_all(class_='picCore pic-Core-v')
    product_link =  soup.find_all(class_='history-item product ')
    if len(product_title) > 0:
        dic = {}
        dic['title'] = product_title[0]['title']
        dic['price'] = float(product_price[0].get_text().replace('US $', '').split(' ')[0])
        dic['image'] = product_image[0]['src']
        dic['link'] = product_link[0]['href']
        list_aliexpress.append(dic)
    return list_aliexpress
