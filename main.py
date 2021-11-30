import requests
from bs4 import BeautifulSoup
import smtplib

url = "AMAZON ITEM URL"
header = {"Accept-Language": "CHECK FROM http://myhttpheader.com/",
           "User-Agent": "CHECK FROM http://myhttpheader.com/"
}

response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.text, "lxml")

price = soup.find(name="span", class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
# print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
# print(title)

buy_price = 300

if price_as_float < buy_price:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login("YOUR EMAIL", "YOUR PASSWORD")
        connection.sendmail(
            from_addr="YOUR EMAIL",
            to_addrs="YOUR EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
