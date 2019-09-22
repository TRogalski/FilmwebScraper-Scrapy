from scrapy.selector import Selector
from scrapy import Spider
from filmwebSpider.items import Movie


class MovieSpider(Spider):
    name = "movie"
    allowed_domains = ["filmweb.pl"]
    page_number = 2
    start_urls = ["https://www.filmweb.pl/films/search?orderBy=popularity&descending=true&page=1"]
    
    def parse(self, response):
        item = Movie()
        title = response.xpath('//div[@class="filmPreview__originalTitle"]/text()').extract()
        score = response.xpath('//span[@class="rateBox__rate"]/text()').extract()
        score_count = response.xpath('//span[@class="rateBox__votes rateBox__votes--count"]/text()').extract()
        wants_to_see_count = response.xpath('//span[@class="wantToSee__count"]/text()').extract()
        year = response.xpath('//div[@class="filmPreview__extraYear"]/text()').extract()
        
        item['title'] = title
        item['score'] = score
        item['score_count'] = score_count
        item['wants_to_see_count'] = wants_to_see_count
        item['year'] = year
        
        yield item
        
        if self.page_number<=20:
            self.page_number += 1
            next_page = "https://www.filmweb.pl/films/search?orderBy=popularity&descending=true&page=%d" % self.page_number
            yield response.follow(next_page, callback = self.parse)
            
        
        
