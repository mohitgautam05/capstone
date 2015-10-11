import scrapy, urlparse, os
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from tutorial.items import JobItem
from scrapy.utils.response import get_base_url
from scrapy.http import Request
from urlparse import urljoin
from datetime import datetime


class JobSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["www.gen-i.si"]
    start_urls = ["http://www.gen-i.si"]

    def parse(self, response):
        response.selector.remove_namespaces() #
        urls = response.xpath('//@href').extract()#choose all "href", either new websites either webpages on our website
        items = []


        base_url = get_base_url(response) #base url


        for url in urls:
            #we need only webpages, so we remove all websites and urls with strange characters
            if (url[0:4] != "http") and not any(x in url for x in ['%', ':', '?', '&']):

                item = JobItem()
                absolute_url = urlparse.urljoin(base_url,url)
                item["link"] = absolute_url
                if item not in items:
                    items.append(item)

                    yield item
                    yield Request(absolute_url, callback = self.parse)
        #return items