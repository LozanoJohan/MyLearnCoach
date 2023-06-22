from controllers.coursera_scrapper import CourseraScrapper 
from controllers.sia_scrapper import SiaScrapper

scrapper = SiaScrapper()
scrapper.scrap()

if False:
    scrapper = CourseraScrapper()

    scrapper.scrap(4)