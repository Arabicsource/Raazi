# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShamelaCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    author 	    = scrapy.Field()
    book    	= scrapy.Field()
    category	= scrapy.Field() 


class AuthorItem(scrapy.Item):
    full_name   = scrapy.Field()
    died        = scrapy.Field()
    link        = scrapy.Field()
    books       = scrapy.Field()



class BookItem(scrapy.Item):
    title       = scrapy.Field()
    publisher   = scrapy.Field()
    link        = scrapy.Field()