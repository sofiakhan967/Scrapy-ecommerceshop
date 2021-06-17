import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ComputersSpider(CrawlSpider):
    name = 'computers'
    allowed_domains = ['slickdeals.net']
    start_urls = ['https://slickdeals.net/computer-deals']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[@class="itemTitle bp-p-dealLink bp-c-link"]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pagination buttongroup"]/a'), follow=True),
    )

    def parse_item(self, response):
        response.url
        yield{
            'title': response.xpath('normalize-space(//h1/text())').get(),
            'price':response.xpath('//div[@class="dealPrice floatLeft"]/text()').get(),
            'url':response.url
            #'Shipping':response.xpath('//div[@id="detailsDescription"]/b/font/text()').get()
        }
