import requests
from bs4 import BeautifulSoup
import smtplib
import sensitive_info

def send_email(title: str, price: str, link: str):
    email = sensitive_info.my_email
    psw = sensitive_info.password

    message = f"{title}\nPrice: ${price}\n{link}"

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=email, password=psw)
    connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject: Low Price\n\n{message}")
    connection.close()

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
}
url = "https://www.amazon.com.br/LG-UltraGear-34GP63A-B-UltraWide-Displayport/dp/B0DJ88QKWR/ref=sr_1_6?crid=1UP2RIPBPMG7Q&dib=eyJ2IjoiMSJ9.Aiqmxd25gYXHjoJEWLpXkZDw78KhsJtl59tU_hxmB9WICseC2lqPEx5GBn4w6cJTT5Dn_qXMe4hr0FcDH18vCcssg3oGyCKxkPmpI7nvkYzTKxZ0eBCje4e22bSSbSUJWP04-H4T4XA9FHxE-HbMwSwSN4vYsM9DpN-J8wDaG6tyRP7QdpsUcIQcP-QyWGrJ0tY2Kh8IN_HJjU-FmiU5LlYgvRw9pGLd42eIGOp62ptQda0ghyLDel0c-7LBqi1X-Nzc5iyuRnNn-CGqySaNtDJncUALK__IXyPAfwSNZKE.hiHZElq1kDLFvp9Gpwq-PkyllAsNmQEwQ2uQFN5Y3h0&dib_tag=se&keywords=monitor+lg+34+ultrawide+curvo&qid=1751647592&sprefix=monitor+LG+34%2Caps%2C231&sr=8-6&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(name="span", class_="a-offscreen").text
title = soup.find(name="span", class_="a-size-large product-title-word-break").text.strip()

print(price)
print(title)
if float(price[2:-3])<3:
    send_email(title, price, url)