import html
import re
import scrapy
from urllib.parse import urljoin
from scrapy_redis.spiders import RedisSpider


# scraper = create_scraper()
# class CloudMiddleware(object):
#     def process_response(self, request, response, spider):
#         if response.status == 403:
#             new_request = scraper.get(request.url)
#             return new_request


class spider(RedisSpider):
    # handle_httpstatus_list = [301, 302]
    name = "posts"
    redis_key = "BDS_URLS"
    # def start_requests(self):
    #     urls = ['https://m.batdongsan.com.vn/nha-dat-cho-thue/p{}'.format(x) for x in range(1, 9600)]
    #     return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        products = response.xpath("//ul[@id = 'product-list-wap']//li/a/@href").extract()
        for p in products:
            url = urljoin(response.url, p)
            yield scrapy.Request(url, callback=self.parse_details)

    def parse_details(self, response):
        # #for info in response.xpath('*[@class = right divContactName]'):
        name = response.xpath("//div[@class = 'col-right']/h3//text()").extract_first()
        phone = response.xpath("//span[@class = 'numberPhone']/@raw").extract_first()

        email = response.xpath("//*[contains(text(), 'emailSeller')]//text()").extract_first().split("emailSeller: ")[1].split(",")[0].split()
        # #Real Estate Details
        Title = response.xpath("//h1//text()").extract_first()
        # Type = response.xpath("//*[text() = 'Loại tin đăng:']/following-sibling::span//text()").extract_first()
        Address = response.xpath("//*[@class= 'address-title']//text()").extract_first()
        # if Address is None:
        # Address = Address.replace("\n        ","")
        # Address_1 = response.xpath("//*[text() = 'Địa chỉ:']/following-sibling::span//text()").extract_first().strip()
        # if Address_1 is not None:
        # City = Address_1.split(",")[-1].strip()
        # else:
        # City = None
        # else:
        # if Address is not None:
        # City = Address.split(",")[-1]
        # Price = response.xpath("//*[text() = 'Mức giá:']/following-sibling::span//text()").extract_first()
        # Square = response.xpath("//*[text() = 'Diện tích:']/following-sibling::span//text()").extract_first()
        # Floors = response.xpath("//*[text() = 'Số tầng:']/following-sibling::span//text()").extract_first()
        # Rooms = response.xpath("//*[text() = 'Số phòng ngủ:']/following-sibling::span//text()").extract_first()
        # Toilets = response.xpath("//*[text() = 'Số toilet:']/following-sibling::span//text()").extract_first()
        # Law = response.xpath("//*[text() = 'Pháp lý:']/following-sibling::span//text()").extract_first()
        # Direction = response.xpath("//*[text() = 'Hướng nhà:']/following-sibling::span//text()").extract_first()
        # Glitch = response.xpath("//*[text() = 'Mặt tiền:']/following-sibling::span//text()").extract_first()
        # Image = response.xpath("//img[@class = 'img-responsive']/@src").extract_first()
        # print(project_title)

        yield {
            "Title": Title,
            # "Loại tin":Type,
            # "Loại BDS": Type,
            'Người bán': name,
            'Số điện thoại': phone,
            'Email': email,
            # 'Giá' :Price,
            'Địa chỉ': Address,
            # 'Pháp lý': Law,
            # 'Tỉnh\Thành':City,
            # #'Mô tả':Description,
            # 'Diện tích':Square,
            # 'Chiều dài':None,
            # 'Chiều ngang':None,
            # 'Số tầng':Floors,
            # 'Số phòn ngủ':Rooms,
            # 'Số toilet': Toilets,
            # 'Mặt tiền':Glitch,
            # 'Hướng':Direction,
            # 'Ảnh':Image,
            'Url': response.url
        }


from scrapy.crawler import CrawlerProcess

process = CrawlerProcess({
    "REDIS_ITEMS_KEY": "bds_net:items",
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

process.crawl(spider)
process.start()