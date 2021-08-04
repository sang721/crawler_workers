import scrapy
from urllib.parse import urljoin
from scrapy_redis.spiders import RedisSpider
from twisted.internet.task import deferLater
from scrapy.item import Field

class spider(RedisSpider):
    name = 'Cong ty'
    redis_key = "COMPANIES_URLS"

    # def start_requests(self):
    #     start_url = []
    #
    #
    #     for url in urls:
    #         for more in url:
    #             start_url.append(more)
    #     print(start_url)
    #     return [scrapy.Request(url=url, callback=self.parse) for url in start_url]

    def parse(self, response):
        links = response.xpath("//h3/a/@href").extract()
        print(links)
        for link in links:
            url = urljoin(response.url, link)
            yield scrapy.Request(url, callback=self.parse_details)

    def parse_details(self, response):
        company_name = response.xpath("//div[@class = 'col-xs-12 col-md-9']/h2//text()").extract_first()
        MST = response.xpath("//div[text()='Mã số thuế:']/following-sibling::div//text()").extract_first()
        name = response.xpath("//div[text()='Chủ sở hữu:']/following-sibling::div//text()").extract_first()
        phone = response.xpath("//div[text()='Điện thoại:']/following-sibling::div//text()").extract_first()
        condition = response.xpath(
            "//div[text()='Tình trạng hoạt động:']/following-sibling::div//text()").extract_first()
        registation_location = response.xpath(
            "//div[text()='Nơi đăng ký quản lý:']/following-sibling::div/a//text()").extract_first()
        day_of_provide = response.xpath("//div[text()='Ngày cấp:']/following-sibling::div//text()").extract_first()
        company_location = response.xpath(
            "//div[text()='Địa chỉ trụ sở:']/following-sibling::div//text()").extract_first()
        ceo_location = response.xpath(
            "//div[text()='Địa chỉ chủ sở hữu:']/following-sibling::div//text()").extract_first()
        ma_nganh = response.xpath("//strong//text()").extract_first().split(' ', 1)[0].replace('.', '')
        nganh_nghe = response.xpath("//strong//text()").extract_first().split(' ', 1)[1]
        City = \
            response.xpath("//div[text()='Địa chỉ trụ sở:']/following-sibling::div//text()").extract_first().split(",")[
                -1]
        Page = response.request.headers.get('Referer', None)
        if phone is not None:
            yield {
                'Tên Công Ty': company_name,
                'Mã đăng ký : ': MST,
                'Tên chủ sở hữu': name,
                'SĐT': phone,
                'Tình trạng hoạt động': condition,
                'Nơi đăng ký': registation_location,
                'Ngày cấp': day_of_provide,
                'Tỉnh thành': City,
                'Địa chỉ công ty': company_location,
                'Địa chỉ chủ sở hữu': ceo_location,
                'Ngành nghề': nganh_nghe,
                'Mã ngành nghề': ma_nganh,
                'Trang': Page.decode("utf-8")
            }


from scrapy.crawler import CrawlerProcess

process = CrawlerProcess({
    "REDIS_ITEMS_KEY": "company:items",
    "CONCURRENT_REQUESTS": 16,
    "RETRY_TIMES": 1000,
    # 'FEED_URI': 'congty.csv',
    # 'FEED_FORMAT': 'csv',
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

process.crawl(spider)
process.start()
