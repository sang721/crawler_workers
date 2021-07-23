import scrapy 
import json
import pprint
def exception(details,arg):
    try:
        main = details[arg].get('value')
    except:
        main = None
    return main
    
class ChoTotItem(scrapy.Item):
    # define the fields for your item here like:
    Title = scrapy.Field()
    Name = scrapy.Field()
    Description = scrapy.Field()
    Phone_number = scrapy.Field()
    Item_address = scrapy.Field()
    Member_address = scrapy.Field()
    Email = scrapy.Field()
    Ad_type = scrapy.Field()
    Province = scrapy.Field()
    Price = scrapy.Field()
    pass

class spider(scrapy.Spider):
    name = 'Cho tot'
    def start_requests(self):
        x = 20
        urls = []
        while x <= 600000:
            url = 'https://gateway.chotot.com/v1/public/ad-listing?cg=1000&limit=20&o={}'.format(x) 
            url_2 = 'https://gateway.chotot.com/v1/public/ad-listing?o={}&cg=2000&limit=20'.format(x)
            url_3 = 'https://gateway.chotot.com/v1/public/ad-listing?o={}&cg=5000&limit=20'.format(x)
            url_4 = 'https://gateway.chotot.com/v1/public/ad-listing?o={}&cg=7000&limit=20'.format(x)
            url_5 = 'https://gateway.chotot.com/v1/public/ad-listing?o={}&cg=4000&limit=20'.format(x)
            url_6 = 'https://gateway.chotot.com/v1/public/ad-listing?o={}&cg=11010&limit=20'.format(x)
            url_7 = 'https://gateway.chotot.com/v1/public/ad-listing?o={}&cg=6000&limit=20'.format(x)
            url_8 = 'https://gateway.chotot.com/v1/public/ad-listing?o={}&cg=13000&limit=20'.format(x)
            url_9 = 'https://gateway.chotot.com/v1/public/ad-listing?o={}&cg=12000&limit=20'.format(x)
            url_10 = 'https://gateway.chotot.com/v1/public/ad-listing?o={}&cg=14000&limit=20'.format(x)
            url_11 = 'https://gateway.chotot.com/v1/public/ad-listing?o={}&cg=9000&limit=20'.format(x)
            url_12 = 'https://gateway.chotot.com/v1/public/ad-listing?o={}&cg=3000&limit=20'.format(x)
            url_13 = 'https://gateway.chotot.com/v1/public/ad-listing?o={}&cg=8000&limit=20'.format(x)
            urls.append(url)
            urls.append(url_2)
            urls.append(url_3)
            urls.append(url_4)
            urls.append(url_5)
            urls.append(url_6)
            urls.append(url_7)
            urls.append(url_8)
            urls.append(url_9)
            urls.append(url_10)
            urls.append(url_11)
            urls.append(url_12)
            urls.append(url_13)
            x = x +20
        return [scrapy.Request(url = url ,callback=self.parse) for url in urls]
    def parse(self,response):
        data = json.loads(response.body).get('ads')
        for link in data:
            url = "https://gateway.chotot.com/v1/public/ad-listing/{}".format(link.get("list_id"))
            yield scrapy.Request(url,callback = self.parse_details)
    def parse_details(self,response):
        items = dict()
        data = json.loads(response.body).get('ad')
        details = json.loads(response.body).get('ad_params')
        items["Item_address"] =  data['area_name'] + " - " + data['region_name']
        items["Title"] = data["subject"]
        items["Description"] = data['body']
        # items["Ad_type"] = data['category_name']
        items["Province"] = data['region_name']
        try:
            items["Price"] = data["0 đ"]
        except:
            items["Price"] = None
        request =  scrapy.Request(url = "https://gateway.chotot.com/v1/public/profile/{}".format(data.get("account_oid")), callback = self.parse_account)
        request.meta['item'] = items
        return request
    def parse_account(self, response):
        items = response.meta['item']
        data = json.loads(response.body)
        items["Name"] = data.get("full_name")
        items["Phone_number"] = data.get("phone")
        items["Member_address"] = data.get("address")
        items["Name"] = data.get("full_name")
        yield items
        # items["Description"] = details['address'].get('value')
         # items["Description"] = details['address'].get('value')
         # items["Description"] = details['address'].get('value')
        # Law = exception(details,'property_legal_document')
        # Square = exception(details,'size')
        # Width = exception(details,'width')
        # Length = exception(details,'length') 
        # Rooms = exception(details,'rooms')
        # Toilets = exception(details,'toilets') 
        # Direction = exception(details,'direction') 
        # Floors = exception(details,'floors')
        # if not '/' in data.get("price_string"):
         # yield {
                    # "Title":data.get("subject"),
                    # # "Loại tin":data.get("category_name"),
                    # #"Loại BDS": Type,
                    # 'Người bán':data.get("account_name"),
                    # 'Số điện thoại':data.get("phone"),
                    # # 'Giá' :data.get("price_string"),
                    # # 'Giá số': data.get("price"),
                    # 'Địa chỉ':Address,
                    # # 'Pháp lý': Law,
                    # # 'Tỉnh\Thành':data.get("region_name"),
                    # #'Mô tả':data.get("body"),
                    # # 'Diện tích':Square,
                    # # 'Chiều dài':Length,
                    # # 'Chiều ngang':Width,
                    # # 'Số tầng':Floors,
                    # # 'Số phòn ngủ':Rooms,
                    # # 'Số toilet': Toilets,
                    # # 'Mặt tiền':None,
                    # # 'Hướng':Direction,
                    # # 'Ảnh':data.get("images")[0],
                    # 'Url':response.url
                    # }
            


from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner




process_2 = CrawlerProcess({
    'FEED_URI': 'cho_tot.csv',
    'FEED_FORMAT': 'csv',
    'CONCURRENT_REQUESTS' : 32
})
process_2.crawl(spider)
process_2.start()
