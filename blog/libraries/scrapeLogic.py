#!/usr/bin/python3

DEV = False

import requests
import bs4
import dryscrape
import os
import re

def scrape_Lazada(url, alertPrice, getName, getIsPriceUnder):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    priceTag = soup.find("span", { "class" : "price" } )
    price = float(priceTag.text[4:])
    #print(priceTag)
    if getName and (not getIsPriceUnder):
        name = str.strip(soup.find("h1", { "class" : "product-info-name" } ).getText())
        return name
    elif getIsPriceUnder and (not(getName)):
        if price <= alertPrice:
            return True
        else:
            return False
    elif getName and getIsPriceUnder:
        if price <= alertPrice:
            return (name, True)
        else:
            return (name, False)
"""
urlList = ["https://www.lazada.sg/xiaomi-redmi-4x-3gb-32gb-gold-20499139.html?spm=a2o42.prod.0.0.18feea70Ul1BP0"]
priceList = [199]

for i in range(len(urlList)):
    if scrape_Lazada(urlList[i], priceList[i]) == 1:
        os.system("firefox "+urlList[i])
url = "https://www.lazada.sg/xiaomi-redmi-4a-32gb-dual-sim-grey-export-17598693.html?spm=a2o42.campaign.list.8.f906417QwzOTF"
"""


def scrape_Taobao_dev(url, alertPrice, getName, getIsPriceUnder):
    session = dryscrape.Session()
    session.visit(url)
    response = session.body()
    soup = bs4.BeautifulSoup(response, "html.parser")
    try:
        price = float(soup.find(id='J_PromoPriceNum').getText())
    except AttributeError as error:
        price = float(soup.find('input', {'name': 'current_price'}).get('value'))
    #print(price)
    if getName and (not getIsPriceUnder):
        name = str.strip(soup.find("h3", { "class" : "tb-main-title" } ).getText())
        return name
    elif getIsPriceUnder and (not(getName)):
        if price <= alertPrice:
            return True
        else:
            return False
    elif getName and getIsPriceUnder:
        if price <= alertPrice:
            return (name, True)
        else:
            return (name, False)


def scrape_Taobao(url, alertPrice, getName, getIsPriceUnder):
    dryscrape.start_xvfb()
    session = dryscrape.Session()
    session.visit(url)
    response = session.body()
    soup = bs4.BeautifulSoup(response, "html.parser")
    try:
        price = float(soup.find(id='J_PromoPriceNum').getText())
    except AttributeError as error:
        price = float(soup.find('input', {'name': 'current_price'}).get('value'))
    #print(price)
    if getName and (not getIsPriceUnder):
        name = str.strip(soup.find("h3", { "class" : "tb-main-title" } ).getText())
        return name
    elif getIsPriceUnder and (not(getName)):
        if price <= alertPrice:
            return True
        else:
            return False
    elif getName and getIsPriceUnder:
        if price <= alertPrice:
            return (name, True)
        else:
            return (name, False)


def scrape_Qoo10(url, alertPrice, getName, getIsPriceUnder):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    priceTag = soup.find("span", { "itemprop" : "price" } )
    price = float(priceTag.text)
    #print(price)
    if getName and (not getIsPriceUnder):
        name = str.strip(soup.find("h2", { "id" : "goods_name" } ).getText())
        return name
    elif getIsPriceUnder and (not(getName)):
        if price <= alertPrice:
            return True
        else:
            return False
    elif getName and getIsPriceUnder:
        if price <= alertPrice:
            return (name, True)
        else:
            return (name, False)


"""
url = "https://item.taobao.com/item.htm?spm=a21wu.241046-sg.4691948847.21.62ab7c25FvwYS6&scm=1007.15423.84311.100200300000005&id=556641227680&pvid=c06bb195-261c-43a9-bcae-b559c9b1d54c"
scrape_Taobao(url, 100)
url = "https://item.taobao.com/item.htm?spm=a21wu.241046-sg.3899615371.2.62ab7c25FvwYS6&id=557049543640"
scrape_Taobao(url, 100)

os.chdir("/home/huang/grow/pythonfiles/lazada_track")
with open("taobao.txt", "w") as txtfile:
    txtfile.write(response)
"""

def scrape_all(url, alertPrice, getName, getIsPriceUnder):
    if "lazada.sg" in url:
        return scrape_Lazada(url, alertPrice, getName, getIsPriceUnder)
    elif "qoo10.sg" in url:
        return scrape_Qoo10(url, alertPrice, getName, getIsPriceUnder)
    elif "taobao.com" in url:
        if DEV == False:
            return scrape_Taobao(url, alertPrice, getName, getIsPriceUnder)
        else:
            return scrape_Taobao_dev(url, alertPrice, getName, getIsPriceUnder)


