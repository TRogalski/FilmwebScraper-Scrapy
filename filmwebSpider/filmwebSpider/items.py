import scrapy


class Movie(scrapy.Item):
    title = scrapy.Field()
    score = scrapy.Field()
    score_count = scrapy.Field()
    wants_to_see_count = scrapy.Field()
    year = scrapy.Field()
