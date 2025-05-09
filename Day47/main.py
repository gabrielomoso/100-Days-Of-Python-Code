import requests
from bs4 import BeautifulSoup
from message import Message

message = Message()

AMAZON_LINK = "https://www.amazon.com/REDMAGIC-Smartphone-Snapdragon-Dual-Sim-Unlocked/dp/B0CP7KJQD5/ref=sr_1_3?crid=29NR93XR9S0VV&dib=eyJ2IjoiMSJ9.-JyUAmIsOk6AD6LFeaGrypq7rABQNOxMcliPbjvYHSPerLGl7A3CgKeWvDnig7sURdgkOV8bfV883KaN07tbzMFy3gvrQ1D4kojC8KubK5oxOd6JFvDPSbcENi3JN4VcI8X0QKmqsEGzC7ciFMNXs_ixbS5D2Yjkehmq5X8BO82kOkdUBCBxi6hh48O4MMXog3U4T-iUkkollc9zEZMqOsKVTIjbPc65ZmOfDcj-x1o.D7hdvMxyLrxdK3-TKAC4CSdpb7tXD52l-6UQGbyaR-M&dib_tag=se&keywords=redmagic%2B9%2Bpro&qid=1707919019&sprefix=REDMA%2Caps%2C549&sr=8-3&th=1"
BUDGET_PRICE = 700


HEADER = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}


response = requests.get(url=AMAZON_LINK, headers=HEADER)
response.raise_for_status()
website = BeautifulSoup(response.text, "html.parser")

product_price = website.find(class_='a-offscreen').text.split("$")[1]
if "," in product_price:
    product_price = float(product_price.replace(",", ""))
else:
    product_price = float(product_price)

product_name = website.find(id="productTitle").getText().strip()

if product_price <= BUDGET_PRICE:
    message.send_mail(name=product_name, price=product_price, link=AMAZON_LINK)
else:
    print(f"The current price of this product is at {product_price}")
    print(f"I will send you an email once it gets below {BUDGET_PRICE}")