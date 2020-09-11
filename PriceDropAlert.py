import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07KXCH2FP?ref_=Oct_DLandingS_D_df3f3913_60&smid=A14CZOWI0VEHLG'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_dealprice").get_text()
    converted_price = float(price[2:4])
    print(converted_price)
    print(title.strip())

    if (converted_price < 50):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('kprathamesh36@gmail.com', 'wgrtcvkkkxhfwpmx')
    subject = "Price Drop Alert"
    body = "Check the amazon link  : https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07KXCH2FP?ref_=Oct_DLandingS_D_df3f3913_60&smid=A14CZOWI0VEHLG"
    msg = f"Subject : {subject}\n\n{body}"
    server.sendmail(
        'kprathamesh36@gmail.com',
        'kprathamesh36@gmail.com',
        msg
    )
    print("EMAIL HAS BEEN SENT!")
    server.quit()

while(True):
    check_price()
    time.sleep(3600)

