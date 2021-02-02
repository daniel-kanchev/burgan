import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from burgan.items import Article


class BurgSpider(scrapy.Spider):
    name = 'burg'
    allowed_domains = ['burgan.com.tr']
    start_urls = ['https://www.burgan.com.tr/tr/Pages/basin-odasi.aspx']

    def parse(self, response):
        articles = response.xpath('//div[@class="grid_12 accordeon-div"]//li')
        for article in articles:
            item = ItemLoader(Article())
            item.default_output_processor = TakeFirst()

            link = article.xpath('.//a/@href').get()
            title = article.xpath('.//a/text()').get()
            date = article.xpath('./text()').getall()[-1]

            item.add_value('title', title)
            item.add_value('date', date)
            item.add_value('link', response.urljoin(link))

            yield item.load_item()
