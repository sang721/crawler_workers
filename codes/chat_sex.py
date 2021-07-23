import requests
from lxml import html
import re
import time
import csv
import pendulum

while True:
    time.sleep(5)
    with open(f"{pendulum.now().to_date_string()}.csv", "w", encoding = "utf-8") as csv_file:
        response = requests.get("https://www6.cbox.ws/box/?boxid=852757&boxtag=99QzDx")
        tree = html.fromstring(response.text)
        regex_pattern = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
        message = tree.xpath("(//div[@class = 'body'])[last()]//text()")
        message = "".join(message)
        member  = tree.xpath("(//div[@class = 'nme'])[last()]//text()")[0]
        phone = re.search(regex_pattern, message)
        if phone is not None:
            phone = phone.group(0)
            csv_file.write(f"{member}| {phone}| {message}")
            print(f"{member}| {phone}| {message}")
            
