#!/usr/bin/env python

import urllib
import urllib2
import smtplib
import json
from email.mime.text import MIMEText
import time

import logger

class GoldPrice:



    REST_URL = "http://quote.forex.hexun.com/rest1/quote_json.ashx?list=XAUUSD"
    ICBC_URL = "https://mybank.icbc.com.cn/servlet/AsynGetDataServlet"
    SMTP_SERVER = "smtp.qq.com"
    USER = "55674645467"
    PASSWORD = "567474453535"
    FROM_ADDR = "sm7989e@qq.com"
    TO_ADDR = "sma567464656q.com"

    def __init__(self):
        pass

    def getICBCData(self):
        paramData = {
            "tranCode": "A00462",
            "Area_code": "0200"
        }
        request = urllib2.Request(self.ICBC_URL, urllib.urlencode(paramData))
        try:
            response = urllib2.urlopen(request)
        except Exception, e:
            logger.logger.error(e)
            return 1
        result = response.read()
        self.ICBCData = json.loads(result.decode("gbk"))
        if self.ICBCData.has_key("market"):
            return 0

    def getPrice(self):
        try:
            return self.ICBCData["market"][4]["middleprice"]
        except Exception, e:
            logger.logger.error(e)


    def setMessage(self, content):
        self.message = MIMEText(content, "plain", "utf-8")
        self.message["From"] =  self.FROM_ADDR
        self.message["To"] = self.TO_ADDR
        self.message["Subject"] = "Warning: Gold Price now is %s" % self.ICBCData["market"][4]["middleprice"]

    def sendMail(self):
        sm = smtplib.SMTP(self.SMTP_SERVER)
        sm.starttls()
        code = sm.ehlo()
        logger.logger.info(sm)
        logger.logger.info(code)
        sm.login(self.USER, self.PASSWORD)
        sm.sendmail(646545653453@qq.com", "6546453534243@qq.com", self.message.as_string())

    def auth(self):
        pass

    def big(self, thresh):
        diff = float(self.ICBCData["market"][4]["openprice_dv"])
        if diff > thresh or diff < - thresh:
            return True

    def below(self, dollar):
        if float(self.ICBCData["market"][4]["middleprice"]) < dollar:
            return True

def start():
    flagBig = 0
    gp = GoldPrice()
 
    while True:
        if gp.getICBCData() == 0:
            logger.logger.info(gp.getPrice())
            if (gp.big(10) and flagBig == 0) or (not gp.big(9) and flagBig == 1):
                content = "Gold Price: " + gp.getPrice()
                gp.setMessage(content)
                gp.sendMail()
                flagBig = 1 - flagBig
        else:
            logger.logger.error("Get data error.")
        time.sleep(30)



if __name__ == "__main__":
    start()
