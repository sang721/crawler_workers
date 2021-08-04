import scrapy
from urllib.parse import urljoin
from scrapy.crawler import CrawlerProcess


class spider(scrapy.Spider):
    name = "Google Map scraper"

    def start_requests(self):
        start_urls = ['https://maps123.net/en/VN/1594446-an-giang',
                      'https://maps123.net/en/VN/1584534-ba-ria-vung-tau',
                      'https://maps123.net/en/VN/1905419-bac-giang',
                      'https://maps123.net/en/VN/1905669-bac-kan',
                      'https://maps123.net/en/VN/1905675-bac-lieu',
                      'https://maps123.net/en/VN/1905412-bac-ninh',
                      'https://maps123.net/en/VN/1587974-ben-tre',
                      'https://maps123.net/en/VN/1905475-binh-duong',
                      'https://maps123.net/en/VN/1587871-binh-dinh',
                      'https://maps123.net/en/VN/1905480-binh-phuoc',
                      'https://maps123.net/en/VN/1581882-binh-thuan',
                      'https://maps123.net/en/VN/1905678-ca-mau',
                      'https://maps123.net/en/VN/1581188-can-tho',
                      'https://maps123.net/en/VN/1586182-cao-bang',
                      'https://maps123.net/en/VN/1905468-da-nng',
                      'https://maps123.net/en/VN/1584169-dak-lak',
                      'https://maps123.net/en/VN/1582720-dong-nai',
                      'https://maps123.net/en/VN/1582562-dong-thap',
                      'https://maps123.net/en/VN/1904987-ak-nong',
                      'https://maps123.net/en/VN/1905099-ien-bien',
                      'https://maps123.net/en/VN/1581088-gia-lai',
                      'https://maps123.net/en/VN/1581030-ha-giang',
                      'https://maps123.net/en/VN/1905637-ha-nam',
                      'https://maps123.net/en/VN/1581129-ha-noi',
                      'https://maps123.net/en/VN/1580700-ha-tinh', 'https://maps123.net/en/VN/1905686-hai-duong',
                      'https://maps123.net/en/VN/1581297-hai-phong', 'https://maps123.net/en/VN/7506719-hau-giang',
                      'https://maps123.net/en/VN/1580578-ho-chi-minh', 'https://maps123.net/en/VN/1572594-hoa-binh',
                      'https://maps123.net/en/VN/1905699-hung-yen', 'https://maps123.net/en/VN/1579634-khanh-hoa',
                      'https://maps123.net/en/VN/1579008-kien-giang', 'https://maps123.net/en/VN/1565088-kon-tum',
                      'https://maps123.net/en/VN/1577954-lai-chau', 'https://maps123.net/en/VN/1577882-lam-dong',
                      'https://maps123.net/en/VN/1576632-lang-son', 'https://maps123.net/en/VN/1562412-lao-cai',
                      'https://maps123.net/en/VN/1575788-long-an', 'https://maps123.net/en/VN/1905626-nam-dinh',
                      'https://maps123.net/en/VN/1559969-nghe-an', 'https://maps123.net/en/VN/1559970-ninh-binh',
                      'https://maps123.net/en/VN/1559971-ninh-thuan', 'https://maps123.net/en/VN/1905577-phu-tho',
                      'https://maps123.net/en/VN/1569805-phu-yen', 'https://maps123.net/en/VN/1568839-quang-binh',
                      'https://maps123.net/en/VN/1905516-quang-nam', 'https://maps123.net/en/VN/1568769-quang-ngai',
                      'https://maps123.net/en/VN/1568758-quang-ninh', 'https://maps123.net/en/VN/1568733-quang-tri',
                      'https://maps123.net/en/VN/1559972-soc-trang', 'https://maps123.net/en/VN/1567643-son-la',
                      'https://maps123.net/en/VN/1566557-tay-ninh-province',
                      'https://maps123.net/en/VN/1566338-thai-binh',
                      'https://maps123.net/en/VN/1905497-thai-nguyen', 'https://maps123.net/en/VN/1566165-thanh-hoa',
                      'https://maps123.net/en/VN/1565033-thua-thien-hue',
                      'https://maps123.net/en/VN/1564676-tien-giang',
                      'https://maps123.net/en/VN/1559975-tra-vinh', 'https://maps123.net/en/VN/1559976-tuyen-quang',
                      'https://maps123.net/en/VN/1559977-vinh-long', 'https://maps123.net/en/VN/1905856-vinh-phuc',
                      'https://maps123.net/en/VN/1559978-yen-bai']

        return [scrapy.Request(url=url, callback=self.parse_url) for url in start_urls]

    def parse_url(self, response):
        links = response.xpath("//div[@class = 'pd']/a/@href").extract()
        return [scrapy.Request(url=url, callback=self.parse_paging) for url in links]

    def parse_paging(self, response):
        paging = response.xpath("(//div[@style= 'width:100%;']//b)[1]//text()").extract_first()
        try:
            paging = int(paging.split(",")[1].replace(" Pages", "")) + 1
            urls = [f"{str(response.url)}?p={x}" for x in range(paging)]
            return [scrapy.Request(url=url, callback=self.parse) for url in urls]
        except AttributeError:
            links = response.xpath("//div[@class = 'pd']/a/@href").extract()
            return [scrapy.Request(url=url, callback=self.parse_link) for url in links]

    def parse_link(self, response):
        paging = response.xpath("(//div[@style= 'width:100%;']//b)[1]//text()").extract_first()
        paging = int(paging.split(",")[1].replace(" Pages", "")) + 1
        urls = [f"{str(response.url)}?p={x}" for x in range(paging)]
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        links = response.xpath("//div[@class = 'pd']/b/a/@href").extract()
        for link in links:
            url = urljoin(response.url, link)
            yield scrapy.Request(url, callback=self.parse_details)

    def parse_details(self, response):
        place_name = response.xpath("//h1//text()").extract_first()
        place_type = response.xpath("//td[@itemprop = 'description']/a//text()").extract_first()
        address = response.xpath("//td[@itemprop = 'address']//text()").extract_first()
        coordinate = response.xpath("//td[@itemprop = 'geo']/a//text()").extract_first()
        phone = response.xpath("//td[@itemprop = 'telephone']//text()").extract_first()
        website = response.xpath(
            '//*[contains(text(), "Website")]/parent::td/following-sibling::td/a//text()').extract_first()
        yield {
            "Loại": place_type,
            "Tên": place_name,
            "Địa chỉ": address,
            "Tọa độ": coordinate,
            "SĐT": phone,
            "Website": website
        }


process_1 = CrawlerProcess(
    settings={
        'FEED_URI': 'maps.csv',
        'FEED_FORMAT': 'csv',
        "ROBOTSTXT_OBEY": False,
        "CONCURRENT_REQUESTS": 32,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 32,
        "CONCURRENT_REQUESTS_PER_IP": 32
    }
)
process_1.crawl(spider)
process_1.start()
