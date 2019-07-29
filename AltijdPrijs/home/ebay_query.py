import requests

def get_list_ebay(query):
    url = 'https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SECURITY-APPNAME=YvesVanc-AltijdPr-PRD-260b1f533-cbdffabe&RESPONSE-DATA-FORMAT=JSON&GLOBAL-ID=EBAY-NLBE&entriesPerPage=3&sortOrder=BestMatch&keywords=' + query #get url for api request
    response = requests.get(url).json()
    list_ebay = []
    if float(response['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]) > 0:
        dic = {}
        dic['title'] = response['findItemsAdvancedResponse'][0]['searchResult'][0]['item'][0]['title'][0] #get title of product
        dic['price'] = float(response['findItemsAdvancedResponse'][0]['searchResult'][0]['item'][0]['sellingStatus'][0]['convertedCurrentPrice'][0]['__value__']) #get price of product
        dic['image'] = response['findItemsAdvancedResponse'][0]['searchResult'][0]['item'][0]['galleryURL'][0] #get image of product
        dic['link'] = response['findItemsAdvancedResponse'][0]['searchResult'][0]['item'][0]['viewItemURL'][0] #get link of product
        list_ebay.append(dic)
    return(list_ebay)



'''
#BeautifulSoup version
import requests
from bs4 import BeautifulSoup

def get_list_ebay(query):
    query = query.replace(' ', '+')
    url = 'https://www.benl.ebay.be/sch/' + query
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    list_ebay = []
    product_title = soup.find_all(class_='lvtitle')
    product_price = soup.find_all(class_ ='lvprice prc')
    product_image = soup.find_all(class_ ='img imgWr2')
    product_link =  soup.find_all(class_='lvtitle')
    if len(product_title) > 0:
        dic = {}
        dic['title'] = product_title[0].get_text().replace('\n','').replace('Nieuwe aanbieding\r\t\t', '')
        dic['price'] = float(product_price[0].get_text().replace('\n','').replace('EUR ','').replace(',', '.').split(' ')[0])
        dic['image'] = product_image[0].img['src']
        dic['link'] = product_link[0].a['href']
        list_ebay.append(dic)
    return(list_ebay)
'''
