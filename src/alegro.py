'''
Created on 6 груд. 2020 р.

@author: jk
'''

if __name__ == '__main__':
    pass


QUERY_OFFER_IMAGE = "img._b8e15_2LNko"
QUERY_OFFER_TITLE = "h1._9a071_1Ux3M"
QUERY_OFFER_PRICE = "div._9a071_2MEB_"
QUERY_OFFER_DESCRIPTION = "div._1h7wt._1l8iq._2d49e_1NgnH"

if __name__ == '__main__':
    pass

from bs4 import BeautifulSoup
import urllib.request
from decimal import Decimal

class Page:
    pageSource = None
    
    def __init__(self, url):
        self.url = url
        self.getPage()

    def getPage(self):
        page = urllib.request.urlopen(self.url)
        resultCode = page.getcode()
        if resultCode == 200:
            self.pageSource = page.read()


class Offer:
    soup = None
    pageSource = None
    url = None
    title = None
    price = None
    description = None
    imagesUrl128 = []
    
    def __init__(self, url):
        self.url = url
        self.getArticlePage()
        self.soup = BeautifulSoup(self.pageSource, 'lxml')
        self.getTitle()
        self.getPrice()
        self.getDescription()
        self.getImagesUrl()
        pass
    
    def getArticlePage(self):
        page = Page(self.url)
        self.pageSource = page.pageSource
        del page
        
    def getTitle(self):
        soupTitle = self.soup.select_one(QUERY_OFFER_TITLE)
        self.title = soupTitle.text
        
    def getPrice(self):
        soupPrice = self.soup.select_one(QUERY_OFFER_PRICE)
        strPrice = soupPrice.text
        strPrice = strPrice.replace("zł", "").replace(",", ".").strip()
        price = Decimal(strPrice)
        self.price = price
        
    def getDescription(self):
        soupDescription = self.soup.select_one(QUERY_OFFER_DESCRIPTION)
        description = soupDescription.getText(strip = True)
        self.description = description                
        
    def getImagesUrl(self):
        soupImages = self.soup.select(QUERY_OFFER_IMAGE)
        for soupImage in soupImages:
            src = soupImage.attrs["src"]
            self.imagesUrl128.append(src)


offer = Offer("https://allegro.pl/oferta/nagrzewnica-samochodowa-farelka-webasto-12v-200w-9864249722")