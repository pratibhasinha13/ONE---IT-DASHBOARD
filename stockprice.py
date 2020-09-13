import re
import time
import urllib
from urllib.request import Request

def stockprice():
    #stock=str(raw_input('Enter Stock Symbol: '))
    hdr= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}

    url= Request('https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=TATASTEEL&illiquid=0&smeFlag=0&itpFlag=0',headers=hdr)
    nav=urllib.request.urlopen(url)
    data=nav.read()

    srch='"lastPrice":"(.*?)"'
    
    com=re.compile(srch)
    rslt=re.findall(com,str(data))
    if(rslt):
        print('' +str(rslt))



while True:
        stockprice()
        time.sleep(5)
