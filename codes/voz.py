
import scrapy 
import json
from lxml import html
import re
from urllib.parse import urljoin
from urllib.request import urlretrieve
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
class voz(scrapy.Spider):
    name = 'Voz forums'
    
    def start_requests(self):
        start_urls = [["https://voz.vn/whats-new/posts/page-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/-/create-threadpage-{}".format(x) for x in range(1,500)],
["https://voz.vn/#dai-sanh.1page-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/thong-bao.2/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/noi-quy-cua-dien-dan-chi-tiet-tung-muc.1583/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/gop-y.3/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/gioi-han-mo-tao-acc-moi-thang-mot-lan.201092/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/s/tin-tuc-inet.102/page-{}".format(x) for x in range(1,500)],
["https://voz.vn/s/105/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/mia-mai-iphone-12-xiaomi-cung-bo-cu-sac.202451/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/s/review-san-pham.103/page-{}".format(x) for x in range(1,500)],
["https://voz.vn/s/106/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/danh-gia-ab-2020-125-sau-nua-nam-trai-nghiem.203717/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/s/chia-se-kien-thuc.104/page-{}".format(x) for x in range(1,500)],
["https://voz.vn/s/107/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/counter-strike-global-offensive-csgo-de-tro-thanh-dai-bang-lua.28124/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/#may-tinh.5page-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/tu-van-cau-hinh.70/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/ngan-sach-50tr-tu-van-cau-hinh-dung-phim-bang-adobe-ma-voi-chip-xeon-va-ram-ecc.204410/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/overclocking-cooling-modding.6/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/nen-chon-aio-hay-air-cooling.189053/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/amd.25/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/box-4-banh-co-qua-theme-box-hoanh-trang-qua-anh-em-box-amd-co-khi-to-chuc-xin-thim-tu-cai-banner-box.105953/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/intel.24/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/neu-mua-i5-10400-hay-i5-10400f-nho-mua-dung-phien-ban-dung-stim.55299/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/gpu-man-hinh.8/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/review-con-rtx-3070-colorful-nb-v-gia-14-5tr.201241/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/phan-cung-chung.9/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/co-thim-nao-da-va-dang-sai-workstation-cu-de-kiem-com-chua.204365/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/thiet-bi-ngoai-vi-phu-kien-mang.30/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/lan-giga-la-toc-do-bao-nhieu.200667/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/server-nas-render-farm.83/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/loi-share-file-tren-windows-server-2016.204637/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/small-form-factor-pc.61/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/lap-hoi-formd-t1-chia-se-anh-thong-tin-build-tu-suong-kho-ram-voi-nhau.136378/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/hackintosh.62/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/thanh-qua-hackintosh-cua-anh-em.8792/unreadpage-{}".format(x) for x in range(1,500)],


["https://voz.vn/f/may-tinh-xach-tay.47/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/tu-van-laptop-tu-15-25-trieu-voi-a.204520/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/#phan-mem-games.20page-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/phan-mem.13/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/nen-dung-premiere-pro-hay-davinci-resolve-dung-after-effects-hay-fusion.204633/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/app-di-dong.21/page-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/lien-quan-mobile.88/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/co-ai-gia-roi-ma-van-choi-lien-quan-khong.194383/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/pc-gaming.11/page-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/lien-minh-huyen-thoai.87/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/genshin-impact-chinh-thuc-phat-hanh-game-the-gioi-mo-da-nen-tang-pc-mobile-ps4-vn-sub.129441/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/console-gaming.22/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/playstation-5-only-demons-souls-remake-2020-launch-rpg-souls.134863/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/#san-pham-cong-nghe.46page-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/android.32/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/mia-mai-iphone-12-xiaomi-cung-bo-cu-sac.202451/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/apple.36/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/iphone-8plus-3-nam-van-chien-moi-loai-game.204411/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/multimedia.31/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/can-tu-van-tai-nghe-over-ear-khoang-5tr.203952/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/do-dien-tu-thiet-bi-gia-dung.10/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/official-thread-ve-diy-may-moc-va-dung-cu-diy.38818/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/chup-anh-quay-phim.75/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/hoi-may-anh-sony-mirrorless-2020.4390/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/#hoc-tap-su-nghiep.89page-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/ngoai-ngu.90/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/ai-hoc-tieng-phap-vao-tro-chuyen-cho-vui-discuter-de-tout-en-francais.204640/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/lap-trinh-cntt.91/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/ung-vien-it-hay-nam-vung-o-dau-cac-bac-nhi.203976/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/kinh-te-luat.92/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/samurai-tung-guom-toe-mau.198406/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/make-money-online.93/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/sale-cua-san-tim-introducing-broker-de-hop-tac.201822/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/tien-dien-tu.94/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/luc-nay-khong-muc-bitcoin-con-doi-luc-nao.7705/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/#khu-vui-choi-giai-tri.16page-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/chuyen-tro-linh-tinh.17/page-{}".format(x) for x in range(1,2400)],

["https://voz.vn/t/thot-show-tien-cua-rmit-boy-trum1k1-bay-mau-roi-a.204512/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/diem-bao.33/page-{}".format(x) for x in range(1,4100)],

["https://voz.vn/t/cap-doi-mac-dong-phuc-hoc-sinh-than-nhien-may-mua-giua-ban-ngay-trong-cong-vien-o-ha-noi-gay-xon-xao.204606/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/4-banh.38/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/outlander-2-0-cvt-lan-banh-tinh-828.185211/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/2-banh.39/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/nguoi-dung-khen-cong-nghe-tren-exciter-155-che-vi-thieu-phanh-abs.204224/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/the-duc-the-thao.63/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/ghi-ban-phut-bu-gio-man-utd-len-nhi-bang-ngoai-hang-anh.204290/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/am-thuc-du-lich.64/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/caffe-tai-gia.2639/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/phim-nhac-sach.65/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/one-piece-wanpiisu-manga-anime.3150/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/thoi-trang-lam-dep.66/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/dong-ho-deo-tay-nam-thao-luan-tu-van-ver-4-1.1318/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/cac-thu-choi-khac.67/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/mua-daniel-wellington-o-dau-cho-yen-tam.204269/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/#khu-thuong-mai.84page-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/may-tinh-de-ban.68/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/dell-optiplex-3020-cau-hinh-i3-i5-i7-gia.14763/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/may-tinh-xach-tay.72/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/dell-latitude-5480-i7-6820hq-ram-8gb-ssd-256gb-vga-roi-2g-nvidia-gt930mx-man-14-fhd-ips.194641/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/dien-thoai-di-dong.76/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/ban-dien-thoai-nap-gap-energizer-e20-ko-dung.196179/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/xe-cac-loai.77/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/hyundai-santafe-2020-cac-phien-ban-dong-loat-giam-gia-kip-uu-dai-thue-trong-nam-2020.196583/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/thoi-trang-lam-dep.78/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/donq-vn-vi-da-va-day-dong-ho-handmade.191642/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/bat-dong-san.79/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/van-phong-ao-quan-3-giai-phap-toi-uu-chi-phi-cho-doanh-nghiep-nho.204621/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/an-uong-du-lich.81/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/nguoi-benh-than-tuyet-doi-khong-uong-mass-gain-muscle.198619/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/sim-so-do-phong-thuy.82/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/thanh-ly.192401/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/f/san-pham-dich-vu-khac.80/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/lam-web-shop-ban-hang-dep-nhu-shopee-gia-re.2966/unreadpage-{}".format(x) for x in range(1,500)],

["https://voz.vn/whats-new/posts/?skip=1page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/samurai-tung-guom-toe-mau.198406/unreadpage-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/kinh-te-luat.92/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/nguoi-dung-khen-cong-nghe-tren-exciter-155-che-vi-thieu-phanh-abs.204224/unreadpage-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/2-banh.39/page-{}".format(x) for x in range(1,500)],

["https://voz.vn/t/outlander-2-0-cvt-lan-banh-tinh-828.185211/unreadpage-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/4-banh.38/page-{}".format(x) for x in range(1,500)],
["https://voz.vn/t/one-piece-wanpiisu-manga-anime.3150/unreadpage-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/phim-nhac-sach.65/page-{}".format(x) for x in range(1,500)],
["https://voz.vn/t/iphone-8plus-3-nam-van-chien-moi-loai-game.204411/unreadpage-{}".format(x) for x in range(1,500)],
["https://voz.vn/f/apple.36/page-{}".format(x) for x in range(1,500)],
["https://voz.vn/whats-new/profile-posts/?skip=1page-{}".format(x) for x in range(1,500)],]

        return [scrapy.Request(url = url ,callback=self.parse) for url in [url for urls in start_urls for url in urls]]
    def parse(self,response):
        data = response.xpath("//div[@class = 'structItem-title']/a/@href").extract()
        if len(data) < 5:
            pass
        else:
            for link in data:
                url = urljoin(response.url, link)
                yield scrapy.Request(url, callback=self.parse_details)
    def parse_details(self,response):
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
                "replied":replied,
                "posted_time":time_posted,
                #"attachment_links":attachment_urls,
                "link":response.url

            }
        if next_page_url:
            print(next_page_url)
            yield response.follow(url=next_page_url, callback=self.parse_details)

































process_2 = CrawlerProcess({
    'FEED_URI': 'voz.csv',
    'FEED_FORMAT': 'csv',
})
process_2.crawl(voz)
process_2.start()
