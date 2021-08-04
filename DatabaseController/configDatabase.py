thien_dia = [['https://hangdep.cc/forums/chuyen-tro-linh-tinh-tm.6/page-{}'.format(x) for x in range(1, 1411)],
             ['https://hangdep.cc/forums/phim-sex-clip-sex.11/page-{}'.format(x) for x in range(1, 155)],
             ['https://hangdep.cc/forums/anh-sex-hinh-sex.8/page-{}'.format(x) for x in range(1, 155)],
             ['https://hangdep.cc/forums/nhat-ky-may-mua.7/page-{}'.format(x) for x in range(1, 155)],
             ['https://hangdep.cc/forums/hoi-dap-linh-tinh-tm.10/page-{}'.format(x) for x in range(1, 155)],
             ['https://hangdep.cc/forums/gai-goi-ha-noi.2/page-{}'.format(x) for x in range(1, 155)],
             ['https://hangdep.cc/forums/gai-goi-sai-gon.3/page-{}'.format(x) for x in range(1, 155)]
             ]

map_vn = ['https://maps123.net/en/VN/1594446-an-giang',
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
          'https://maps123.net/en/VN/1566557-tay-ninh-province', 'https://maps123.net/en/VN/1566338-thai-binh',
          'https://maps123.net/en/VN/1905497-thai-nguyen', 'https://maps123.net/en/VN/1566165-thanh-hoa',
          'https://maps123.net/en/VN/1565033-thua-thien-hue', 'https://maps123.net/en/VN/1564676-tien-giang',
          'https://maps123.net/en/VN/1559975-tra-vinh', 'https://maps123.net/en/VN/1559976-tuyen-quang',
          'https://maps123.net/en/VN/1559977-vinh-long', 'https://maps123.net/en/VN/1905856-vinh-phuc',
          'https://maps123.net/en/VN/1559978-yen-bai']

my_companies_list = [['https://doanhnghiepmoi.vn/Ha-Noi/trang-%s/' % page for page in range(1, 19210)],
                     ['https://doanhnghiepmoi.vn/TP-Ho-Chi-Minh/trang-%s/' % page for page in range(1, 31077)],
                     ['https://doanhnghiepmoi.vn/Can-Tho/trang-%s/' % page for page in range(1, 1181)],
                     ['https://doanhnghiepmoi.vn/Da-Nang/trang-%s/' % page for page in range(1, 2818)],
                     ['https://doanhnghiepmoi.vn/Hai-Phong/trang-%s/' % page for page in range(1, 2727)],
                     ['https://doanhnghiepmoi.vn/An-Giang/trang-%s/' % page for page in range(1, 900)],
                     ['https://doanhnghiepmoi.vn/Ba-Ria-Vung-Tau/trang-%s/' % page for page in range(1, 1135)],
                     ['https://doanhnghiepmoi.vn/Bac-Can/trang-%s/' % page for page in range(1, 135)],
                     ['https://doanhnghiepmoi.vn/Bac-Giang/trang-%s/' % page for page in range(1, 784)],
                     ['https://doanhnghiepmoi.vn/Bac-Kan/trang-%s/' % page for page in range(1, 35)],
                     ['https://doanhnghiepmoi.vn/Bac-Lieu/trang-%s/' % page for page in range(1, 323)],
                     ['https://doanhnghiepmoi.vn/Bac-Ninh/trang-%s/' % page for page in range(1, 1238)],
                     ['https://doanhnghiepmoi.vn/Ben-Tre/trang-%s/' % page for page in range(1, 501)],
                     ['https://doanhnghiepmoi.vn/Binh-Duong/trang-%s/' % page for page in range(1, 3271)],
                     ['https://doanhnghiepmoi.vn/Binh-Phuoc/trang-%s/' % page for page in range(1, 703)],
                     ['https://doanhnghiepmoi.vn/Binh-Thuan/trang-%s/' % page for page in range(1, 670)],  # file 5
                     ['https://doanhnghiepmoi.vn/Binh-Dinh/trang-%s/' % page for page in range(1, 806)],  # file 5
                     ['https://doanhnghiepmoi.vn/Binh-Dinh/trang-%s/' % page for page in range(1, 806)],  # file 5
                     ['https://doanhnghiepmoi.vn/Ca-Mau/trang-%s/' % page for page in range(1, 647)],  # file 5
                     ['https://doanhnghiepmoi.vn/Cao-Bang/trang-%s/' % page for page in range(1, 222)],  # file 5
                     ['https://doanhnghiepmoi.vn/Gia-Lai/trang-%s/' % page for page in range(1, 636)],  # file 5
                     ['https://doanhnghiepmoi.vn/Ha-Giang/trang-%s/' % page for page in range(1, 284)],
                     ['https://doanhnghiepmoi.vn/Ha-Nam/trang-%s/' % page for page in range(1, 447)],
                     ['https://doanhnghiepmoi.vn/Ha-Tinh/trang-%s/' % page for page in range(1, 660)],
                     ['https://doanhnghiepmoi.vn/Hai-Duong/trang-%s/' % page for page in range(1, 1175)],
                     ['https://doanhnghiepmoi.vn/Hau-Giang/trang-%s/' % page for page in range(1, 352)],
                     ['https://doanhnghiepmoi.vn/Hoa-Binh/trang-%s/' % page for page in range(1, 425)],
                     ['https://doanhnghiepmoi.vn/Hue/trang-%s/' % page for page in range(1, 126)],
                     ['https://doanhnghiepmoi.vn/Hung-Yen/trang-%s/' % page for page in range(1, 806)],  # file 5
                     ['https://doanhnghiepmoi.vn/Khanh-Hoa/trang-%s/' % page for page in range(1, 1344)],  # file 5
                     ['https://doanhnghiepmoi.vn/Kien-Giang/trang-%s/' % page for page in range(1, 1047)],  # file 5
                     ['https://doanhnghiepmoi.vn/Kon-Tum/trang-%s/' % page for page in range(1, 311)],  # file 5
                     ['https://doanhnghiepmoi.vn/Lai-Chau/trang-%s/' % page for page in range(1, 205)],
                     ['https://doanhnghiepmoi.vn/Lam-Dong/trang-%s/' % page for page in range(1, 919)],
                     ['https://doanhnghiepmoi.vn/Lang-Son/trang-%s/' % page for page in range(1, 355)],
                     ['https://doanhnghiepmoi.vn/Lao-Cai/trang-%s/' % page for page in range(1, 427)],
                     ['https://doanhnghiepmoi.vn/Long-An/trang-%s/' % page for page in range(1, 1293)],
                     ['https://doanhnghiepmoi.vn/Nam-Dinh/trang-%s/' % page for page in range(1, 727)],
                     ['https://doanhnghiepmoi.vn/Nghe-An/trang-%s/' % page for page in range(1, 1435)],
                     ['https://doanhnghiepmoi.vn/Ninh-Binh/trang-%s/' % page for page in range(1, 512)],
                     ['https://doanhnghiepmoi.vn/Ninh-Thuan/trang-%s/' % page for page in range(1, 355)],
                     ['https://doanhnghiepmoi.vn/Phu-Tho/trang-%s/' % page for page in range(1, 669)],
                     ['https://doanhnghiepmoi.vn/Phu-Yen/trang-%s/' % page for page in range(1, 422)],
                     ['https://doanhnghiepmoi.vn/Quang-Binh/trang-%s/' % page for page in range(1, 557)],
                     ['https://doanhnghiepmoi.vn/Quang-Nam/trang-%s/' % page for page in range(1, 947)],
                     ['https://doanhnghiepmoi.vn/Quang-Ngai/trang-%s/' % page for page in range(1, 653)],
                     ['https://doanhnghiepmoi.vn/Quang-Ninh/trang-%s/' % page for page in range(1, 1256)],
                     ['https://doanhnghiepmoi.vn/Quang-Tri/trang-%s/' % page for page in range(1, 409)],
                     ['https://doanhnghiepmoi.vn/Soc-Trang/trang-%s/' % page for page in range(1, 407)],
                     ['https://doanhnghiepmoi.vn/Son-La/trang-%s/' % page for page in range(1, 363)],
                     ['https://doanhnghiepmoi.vn/Tay-Ninh/trang-%s/' % page for page in range(1, 700)],
                     ['https://doanhnghiepmoi.vn/Thai-Binh/trang-%s/' % page for page in range(1, 654)],
                     ['https://doanhnghiepmoi.vn/Thai-Nguyen/trang-%s/' % page for page in range(1, 640)],
                     ['https://doanhnghiepmoi.vn/Thanh-Hoa/trang-%s/' % page for page in range(1, 1715)],
                     ['https://doanhnghiepmoi.vn/Thua-Thien-Hue/trang-%s/' % page for page in range(1, 550)],
                     ['https://doanhnghiepmoi.vn/Tien-Giang/trang-%s/' % page for page in range(1, 689)],
                     ['https://doanhnghiepmoi.vn/Tra-Vinh/trang-%s/' % page for page in range(1, 330)],
                     ['https://doanhnghiepmoi.vn/Tuyen-Quang/trang-%s/' % page for page in range(1, 246)],
                     ['https://doanhnghiepmoi.vn/Vinh-Long/trang-%s/' % page for page in range(1, 436)],
                     ['https://doanhnghiepmoi.vn/Vinh-Phuc/trang-%s/' % page for page in range(1, 796)],
                     ['https://doanhnghiepmoi.vn/Vung-Tau/trang-%s/' % page for page in range(1, 255)],
                     ['https://doanhnghiepmoi.vn/Yen-Bai/trang-%s/' % page for page in range(1, 319)],
                     ['https://doanhnghiepmoi.vn/Dac-Lac/trang-%s/' % page for page in range(1, 791)],
                     ['https://doanhnghiepmoi.vn/Dak-Lak/trang-%s/' % page for page in range(1, 92)],
                     ['https://doanhnghiepmoi.vn/Dak-Nong/trang-%s/' % page for page in range(1, 318)],
                     ['https://doanhnghiepmoi.vn/Dien-Bien/trang-%s/' % page for page in range(1, 181)],
                     ['https://doanhnghiepmoi.vn/Dong-Nai/trang-%s/' % page for page in range(1, 2801)],
                     ['https://doanhnghiepmoi.vn/Dong-Thap/trang-%s/' % page for page in range(1, 594)]]

x = 0
urls_cho_tot = []
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
    urls_cho_tot.append(url)
    urls_cho_tot.append(url_2)
    urls_cho_tot.append(url_3)
    urls_cho_tot.append(url_4)
    urls_cho_tot.append(url_5)
    urls_cho_tot.append(url_6)
    urls_cho_tot.append(url_7)
    urls_cho_tot.append(url_8)
    urls_cho_tot.append(url_9)
    urls_cho_tot.append(url_10)
    urls_cho_tot.append(url_11)
    urls_cho_tot.append(url_12)
    urls_cho_tot.append(url_13)
    x = x + 20

BDS_URLS = ['https://m.batdongsan.com.vn/nha-dat-cho-thue/p{}'.format(x) for x in range(1, 9600)]
