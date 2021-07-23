import scrapy
from urllib.parse import urljoin

class spider(scrapy.Spider):
    name = 'Cong ty'
    def start_requests(self):
        start_url =  []
        urls = [['https://doanhnghiepmoi.vn/Ha-Noi/trang-%s/' %page for page in range(1,19210)],
                ['https://doanhnghiepmoi.vn/TP-Ho-Chi-Minh/trang-%s/' %page for page in range(1,31077 )],
                ['https://doanhnghiepmoi.vn/Can-Tho/trang-%s/' %page for page in range(1,1181)],
                ['https://doanhnghiepmoi.vn/Da-Nang/trang-%s/' %page for page in range(1,2818)],#file 4
                ['https://doanhnghiepmoi.vn/Hai-Phong/trang-%s/' %page for page in range(1,2727)],#file 4
                ['https://doanhnghiepmoi.vn/An-Giang/trang-%s/' %page for page in range(1,900)],#file 4
                ['https://doanhnghiepmoi.vn/Ba-Ria-Vung-Tau/trang-%s/' %page for page in range(1,1135)],#file 4
                ['https://doanhnghiepmoi.vn/Bac-Can/trang-%s/' %page for page in range(1,135)],#file 4
                ['https://doanhnghiepmoi.vn/Bac-Giang/trang-%s/' %page for page in range(1,784)],#file 4
                ['https://doanhnghiepmoi.vn/Bac-Kan/trang-%s/' %page for page in range(1,35)],
                ['https://doanhnghiepmoi.vn/Bac-Lieu/trang-%s/' %page for page in range(1,323)],
                ['https://doanhnghiepmoi.vn/Bac-Ninh/trang-%s/' %page for page in range(1,1238)],
                ['https://doanhnghiepmoi.vn/Ben-Tre/trang-%s/' %page for page in range(1,501)],
                ['https://doanhnghiepmoi.vn/Binh-Duong/trang-%s/' %page for page in range(1,3271)],
                ['https://doanhnghiepmoi.vn/Binh-Phuoc/trang-%s/' %page for page in range(1,703)],
                ['https://doanhnghiepmoi.vn/Binh-Thuan/trang-%s/' %page for page in range(1,670)],#file 5
                ['https://doanhnghiepmoi.vn/Binh-Dinh/trang-%s/' %page for page in range(1,806)],#file 5
                ['https://doanhnghiepmoi.vn/Binh-Dinh/trang-%s/' %page for page in range(1,806)],#file 5
                ['https://doanhnghiepmoi.vn/Ca-Mau/trang-%s/' %page for page in range(1,647)],#file 5
                ['https://doanhnghiepmoi.vn/Cao-Bang/trang-%s/' %page for page in range(1,222)],#file 5
                ['https://doanhnghiepmoi.vn/Gia-Lai/trang-%s/' %page for page in range(1,636)],#file 5
                ['https://doanhnghiepmoi.vn/Ha-Giang/trang-%s/' %page for page in range(1,284)],#file 5
                ['https://doanhnghiepmoi.vn/Ha-Nam/trang-%s/' %page for page in range(1,447)],#file 5
                ['https://doanhnghiepmoi.vn/Ha-Tinh/trang-%s/' %page for page in range(1,660)],#file 5
                ['https://doanhnghiepmoi.vn/Hai-Duong/trang-%s/' %page for page in range(1,1175)],#file 5
                ['https://doanhnghiepmoi.vn/Hau-Giang/trang-%s/' %page for page in range(1,352)],#file 5
                ['https://doanhnghiepmoi.vn/Hoa-Binh/trang-%s/' %page for page in range(1,425)],#file 5
                ['https://doanhnghiepmoi.vn/Hue/trang-%s/' %page for page in range(1,126)],#file 5
                ['https://doanhnghiepmoi.vn/Hung-Yen/trang-%s/' %page for page in range(1,806)],#file 5
                ['https://doanhnghiepmoi.vn/Khanh-Hoa/trang-%s/' %page for page in range(1,1344)],#file 5
                ['https://doanhnghiepmoi.vn/Kien-Giang/trang-%s/' %page for page in range(1,1047)],#file 5
                ['https://doanhnghiepmoi.vn/Kon-Tum/trang-%s/' %page for page in range(1,311)],#file 5
                ['https://doanhnghiepmoi.vn/Lai-Chau/trang-%s/' %page for page in range(1,205)],
                ['https://doanhnghiepmoi.vn/Lam-Dong/trang-%s/' %page for page in range(1,919)],
                ['https://doanhnghiepmoi.vn/Lang-Son/trang-%s/' %page for page in range(1,355)],
                ['https://doanhnghiepmoi.vn/Lao-Cai/trang-%s/' %page for page in range(1,427)],
                ['https://doanhnghiepmoi.vn/Long-An/trang-%s/' %page for page in range(1,1293)],
                ['https://doanhnghiepmoi.vn/Nam-Dinh/trang-%s/' %page for page in range(1,727)],
                ['https://doanhnghiepmoi.vn/Nghe-An/trang-%s/' %page for page in range(1,1435)],
                ['https://doanhnghiepmoi.vn/Ninh-Binh/trang-%s/' %page for page in range(1,512)],
                ['https://doanhnghiepmoi.vn/Ninh-Thuan/trang-%s/' %page for page in range(1,355)],
                ['https://doanhnghiepmoi.vn/Phu-Tho/trang-%s/' %page for page in range(1,669)],
                ['https://doanhnghiepmoi.vn/Phu-Yen/trang-%s/' %page for page in range(1,422)],
                ['https://doanhnghiepmoi.vn/Quang-Binh/trang-%s/' %page for page in range(1,557)],
                ['https://doanhnghiepmoi.vn/Quang-Nam/trang-%s/' %page for page in range(1,947)],
                ['https://doanhnghiepmoi.vn/Quang-Ngai/trang-%s/' %page for page in range(1,653)],
                ['https://doanhnghiepmoi.vn/Quang-Ninh/trang-%s/' %page for page in range(1,1256)],
                ['https://doanhnghiepmoi.vn/Quang-Tri/trang-%s/' %page for page in range(1,409)],
                ['https://doanhnghiepmoi.vn/Soc-Trang/trang-%s/' %page for page in range(1,407)],
                ['https://doanhnghiepmoi.vn/Son-La/trang-%s/' %page for page in range(1,363)],
                ['https://doanhnghiepmoi.vn/Tay-Ninh/trang-%s/' %page for page in range(1,700)],
                ['https://doanhnghiepmoi.vn/Thai-Binh/trang-%s/' %page for page in range(1,654)],
                ['https://doanhnghiepmoi.vn/Thai-Nguyen/trang-%s/' %page for page in range(1,640)],
                ['https://doanhnghiepmoi.vn/Thanh-Hoa/trang-%s/' %page for page in range(1,1715)],
                ['https://doanhnghiepmoi.vn/Thua-Thien-Hue/trang-%s/' %page for page in range(1,550)],
                ['https://doanhnghiepmoi.vn/Tien-Giang/trang-%s/' %page for page in range(1,689)],
                ['https://doanhnghiepmoi.vn/Tra-Vinh/trang-%s/' %page for page in range(1,330)],
                ['https://doanhnghiepmoi.vn/Tuyen-Quang/trang-%s/' %page for page in range(1,246)],
                ['https://doanhnghiepmoi.vn/Vinh-Long/trang-%s/' %page for page in range(1,436)],
                ['https://doanhnghiepmoi.vn/Vinh-Phuc/trang-%s/' %page for page in range(1,796)],
                ['https://doanhnghiepmoi.vn/Vung-Tau/trang-%s/' %page for page in range(1,255)],
                ['https://doanhnghiepmoi.vn/Yen-Bai/trang-%s/' %page for page in range(1,319)],
                ['https://doanhnghiepmoi.vn/Dac-Lac/trang-%s/' %page for page in range(1,791)],
                ['https://doanhnghiepmoi.vn/Dak-Lak/trang-%s/' %page for page in range(1,92)],
                ['https://doanhnghiepmoi.vn/Dak-Nong/trang-%s/' %page for page in range(1,318)],
                ['https://doanhnghiepmoi.vn/Dien-Bien/trang-%s/' %page for page in range(1,181)],
                ['https://doanhnghiepmoi.vn/Dong-Nai/trang-%s/' %page for page in range(1,2801)],
                ['https://doanhnghiepmoi.vn/Dong-Thap/trang-%s/' %page for page in range(1,594)]
                ]

        for url in urls:
            for more in url:
                start_url.append(more)
        print(start_url)
        return [scrapy.Request(url=url, callback=self.parse) for url in start_url]
    def parse(self,response):
        links = response.xpath("//h3/a/@href").extract()
        print(links)
        for link in links:
            url = urljoin(response.url, link)
            yield scrapy.Request(url, callback=self.parse_details)
    def parse_details(self,response):
        company_name = response.xpath("//div[@class = 'col-xs-12 col-md-9']/h2//text()").extract_first()
        MST =  response.xpath("//div[text()='Mã số thuế:']/following-sibling::div//text()").extract_first()
        name = response.xpath("//div[text()='Chủ sở hữu:']/following-sibling::div//text()").extract_first()
        phone = response.xpath("//div[text()='Điện thoại:']/following-sibling::div//text()").extract_first()
        condition = response.xpath("//div[text()='Tình trạng hoạt động:']/following-sibling::div//text()").extract_first()
        registation_location = response.xpath("//div[text()='Nơi đăng ký quản lý:']/following-sibling::div/a//text()").extract_first()
        day_of_provide = response.xpath("//div[text()='Ngày cấp:']/following-sibling::div//text()").extract_first()
        company_location = response.xpath("//div[text()='Địa chỉ trụ sở:']/following-sibling::div//text()").extract_first()
        ceo_location = response.xpath("//div[text()='Địa chỉ chủ sở hữu:']/following-sibling::div//text()").extract_first()
        ma_nganh = response.xpath("//strong//text()").extract_first().split(' ',1)[0].replace('.','')
        nganh_nghe = response.xpath("//strong//text()").extract_first().split(' ',1)[1]
        City = response.xpath("//div[text()='Địa chỉ trụ sở:']/following-sibling::div//text()").extract_first().split(",")[-1]
        Page = response.request.headers.get('Referer', None)
        if phone is not None:
            yield {
                'Tên Công Ty' : company_name,
                'Mã đăng ký : ':MST,
                 'Tên chủ sở hữu' : name,
                  'SĐT' : phone,
                  'Tình trạng hoạt động':condition,
                  'Nơi đăng ký':registation_location,
                  'Ngày cấp':day_of_provide,
                  'Tỉnh thành':City,
                  'Địa chỉ công ty':company_location,
                  'Địa chỉ chủ sở hữu':ceo_location,
                  'Ngành nghề':nganh_nghe,
                  'Mã ngành nghề':ma_nganh,
                  'Trang' : Page
            }
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner



process_2 = CrawlerProcess({
    'FEED_URI': 'congty.csv',
    'FEED_FORMAT': 'csv',
})
process_2.crawl(spider)
process_2.start()
