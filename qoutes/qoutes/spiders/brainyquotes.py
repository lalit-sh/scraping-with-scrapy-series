# -*- coding: utf-8 -*-
import scrapy


class BrainyquotesSpider(scrapy.Spider):
    name = 'brainyquotes'
    allowed_domains = ['www.brainyquote.com']

    def start_requests(self):
        urls = [
           'https://www.brainyquote.com/topics/life'
           'https://www.brainyquote.com/topics/motivational'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        quotes = []

        '''This will extract all cards which initially contains our quote'''
        cards = response.xpath('//*[@id="quotesList"]/div')
        
        '''we will loop through cards to extract all the quotes'''
        for card in cards:
            'extracting quote'
            q = card.xpath("//div[1]/div/a[1]/text()").extract_first()

            'extracting writer'
            w = card.xpath("//div[1]/div/a[2]/text()").extract_first()

            ''' storing data to quotes array in json object format '''
            quotes.append({
                "writer": w,
                "quote": q
            })

        print(quotes)
        '''we can further save this data to a file'''
        self.saveQuotes(quotes)
        return quotes

    def saveQuotes(self, quotes):
        file = open("quotes.json", 'w')
        file.write("{ \n \"quotes\" : [ \n")
        for quote in quotes:
            file.write("%s\n" % quote)
        file.write("] \n } \n")
        file.close()