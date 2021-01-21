from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import smtplib
from email.message import EmailMessage
from DjangoPracAkki.pleasedontsee import Email_Address,Email_password

import csv
def script(link, price, email):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(PATH, options=options)
    driver.get(link)
    product_name = driver.find_element_by_id("productTitle").text
    try:
        search = driver.find_element_by_id("priceblock_dealprice").text[1:]
    except:
        search = driver.find_element_by_id("priceblock_ourprice").text[1:]
    if (float(search.replace(',',''))<=float(price)):
        #Email_Address = "vatsals407@gmail.com"
        #Email_password = "sms462890"
        msg = EmailMessage()
        msg['Subject'] = "Price tracker"
        msg['From'] = Email_Address
        msg['To'] = email
        msg.set_content(
            'Notification price of your product = "' + product_name + '" \n price = "' + search + '" \n link = " ' + link + '"')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Email_Address, Email_password)
            smtp.send_message(msg)
    else:
        rows = [[',',link, price, email]]
        filename = "D:\woc python\djangoprac\DjangoPracAkki/amazon.csv"
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            # csvwriter.writerow(fields)
            csvwriter.writerows(rows)