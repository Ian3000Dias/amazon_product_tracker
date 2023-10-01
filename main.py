import smtplib

import requests
from bs4 import BeautifulSoup
import pprint
import lxml
from smtplib import SMTP

URL = "https://www.amazon.in/dp/B09SHYV8VD/ref=nav_custrec_signin?_encoding=UTF8&psc=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.8"
}
USER = "iandias347@gmail.com"
PASSWORD = "uteuawyraegjveis"
response = requests.get(url=URL, headers=header)
response.raise_for_status()
product_web = response.text

# print(product_web)
soup = BeautifulSoup(product_web, "lxml")
price_data = soup.find(name="span", class_="a-price-whole").getText()
name_data = soup.find(name="span", id="productTitle").getText().strip(" ")
price = (float(price_data))

if price < 950:
    message = f"'{name_data}' is now ₹{price} only. Click below link to go to site. \n{URL}"
    print(message)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(
            from_addr="iandias347@gmail.com",
            to_addrs="iandias72@yahoo.com",
            msg=f"Subject:Hello\n\n{message}".encode("utf-8")
        )
