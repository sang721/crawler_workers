import time

import scrapy
import json
from lxml import html
import re
from urllib.parse import urljoin
from scrapy_redis.spiders import RedisSpider


class thien_dia(RedisSpider):
    name = 'Cho tot'
    redis_key = "THIENDIA_URL"

    # def start_requests(self):
    #     start_urls = [['https://hangdep.cc/forums/chuyen-tro-linh-tinh-tm.6/page-{}'.format(x) for x in range(1, 1411)],
    #                   ['https://hangdep.cc/forums/phim-sex-clip-sex.11/page-{}'.format(x) for x in range(1, 155)],
    #                   ['https://hangdep.cc/forums/anh-sex-hinh-sex.8/page-{}'.format(x) for x in range(1, 155)],
    #                   ['https://hangdep.cc/forums/nhat-ky-may-mua.7/page-{}'.format(x) for x in range(1, 155)],
    #                   ['https://hangdep.cc/forums/hoi-dap-linh-tinh-tm.10/page-{}'.format(x) for x in range(1, 155)],
    #                   ['https://hangdep.cc/forums/gai-goi-ha-noi.2/page-{}'.format(x) for x in range(1, 155)],
    #                   ['https://hangdep.cc/forums/gai-goi-sai-gon.3/page-{}'.format(x) for x in range(1, 155)]
    #                   ]
    #     return [scrapy.Request(url=url, callback=self.parse) for url in [url for urls in start_urls for url in urls]]


    def parse(self, response):
        data = response.xpath("//div[@class = 'structItem-title']/a/@href").extract()
        print(data)
        for link in data:
            url = urljoin(response.url, link)
            yield scrapy.Request(url, callback=self.parse_details)

    def parse_details(self, response):
        article_blocks = response.xpath("//div[@class = 'block-body js-replyNewMessageContainer']/article").extract()
        title = response.xpath("//h1[@class = 'p-title-value']//text()").extract_first()
        next_page_url = response.xpath("//a[@class = 'pageNav-jump pageNav-jump--next']/@href").extract_first()
        regex_pattern = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
        for block in article_blocks:
            tree = html.fromstring(block)
            member_link = tree.xpath("//a[@class = 'username ']/@href")[0]
            time_posted = tree.xpath("//time/@data-time")[0]
            time_posted = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time_posted)))
            member_name = tree.xpath("//a[@class = 'username ']//text()")[0]
            try:
                replied = tree.xpath("//div[@class = 'bbCodeBlock-expandContent js-expandContent ']//text()")
                replied = " ".join(replied)
            except:
                replied = ""
            try:
                member_story = tree.xpath("//div[@class = 'bbWrapper']/text()")
                member_story = " ".join(member_story)
            except:
                member_story = ""
            # print(tree.xpath("//time/@data-time")
            # for article in article_blocks:
            #     time_posted = article.xpath("//time/@data-time").extract_first()
            #     time_posted = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time_posted)))
            #     member_name = article.xpath("//a[@class = 'username ']//text()").extract_first()
            #     member_link = article.xpath("//a[@class = 'username ']/@href").extract_first()
            #     members_story = article.xpath("//div[@class = 'bbWrapper']/text()").extract_first()
            #     replied = article.xpath("//div[@class = 'bbCodeBlock-expandContent js-expandContent ']//text()").extract_first()
            #     attachment_urls = article.xpath("//img/@src").extract()
            #     attachment_urls = ", ".join([urljoin(response.url, link) for link in attachment_urls])
            try:
                phone = re.search(regex_pattern, member_story)
                phone = phone.group(0)
            except:
                phone = None
            yield {
                "title": title,
                "members": member_name,
                "member_link": member_link,
                "phone number": phone,
                "stories": member_story,
                "replied": replied,
                "posted_time": time_posted,
                # "attachment_links":attachment_urls,
                "link": response.url

            }
        if next_page_url:
            print(next_page_url)
            yield response.follow(url=next_page_url, callback=self.parse_details)


from scrapy.crawler import CrawlerProcess

process = CrawlerProcess({
    "REDIS_ITEMS_KEY": "thiendia:items",
    "CONCURRENT_REQUESTS": 16,
    "RETRY_TIMES": 1000,
    "ITEM_PIPELINES": {
        'scrapy_redis.pipelines.RedisPipeline': 300
    },
    "REDIS_HOST": "localhost",
    "REDIS_PORT": 6379,
    "REDIS_PARAMS": {
        'password': "usaf",
        "db": 2
    },
})

process.crawl(thien_dia)
process.start()

