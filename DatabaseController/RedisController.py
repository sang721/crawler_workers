import redis
from configDatabase import my_companies_list, urls_cho_tot, map_vn, thien_dia, BDS_URLS

r = redis.Redis(host="localhost", port=6379, password="usaf", db=2)

start_url = []
for url in my_companies_list:
    for more in url:
        start_url.append(more)
for url in start_url:
    r.lpush("COMPANIES_URLS", url)

urls_cho_tot = urls_cho_tot
urls_cho_tot.reverse()
for url in urls_cho_tot:
    r.lpush("CHOTOT_URLS", url)

start_url = []
for url in thien_dia:
    for more in url:
        start_url.append(more)

for url in start_url:
    r.lpush("THIENDIA_URL", url)

BDS_URLS = BDS_URLS
for url in BDS_URLS:
    r.lpush("BDS_URLS", url)
