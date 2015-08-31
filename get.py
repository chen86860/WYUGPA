# -*- coding: UTF-8 -*-
__author__ = '星星'
import urllib
import urllib2
import cookielib
import string

TskUrl = "http://202.192.240.54/tbx/tsk/savesel.aspx"
User_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36"
Refere = "http://202.192.240.54/tbx/tsk/confirm.aspx"

jingguan=[
    "0103950_0_%e5%88%9b%e4%b8%9a%e7%ae%a1%e7%90%86%e4%b8%8e%e5%95%86%e4%b8%9a%e6%a8%a1%e5%bc%8f_0.5",
    "0103980_0_%e5%a4%a7%e5%ad%a6%e7%94%9f%e8%87%aa%e6%88%91%e7%ae%a1%e7%90%86_0.5",
    "0100340_0_%e5%bd%93%e4%bb%a3%e5%9b%bd%e9%99%85%e9%87%91%e8%9e%8d%e5%af%bc%e8%ae%ba_0.5",
    "0100350_0_%e5%bd%93%e4%bb%a3%e5%9b%bd%e9%99%85%e8%b4%b8%e6%98%93%e5%af%bc%e8%ae%ba_0.5",
    "0100350_1_%e5%bd%93%e4%bb%a3%e5%9b%bd%e9%99%85%e8%b4%b8%e6%98%93%e5%af%bc%e8%ae%ba_0.5",
    "0100390_0_%e7%ae%a1%e7%90%86%e7%90%86%e8%ae%ba%e5%af%bc%e8%ae%ba_0.25",
    "0100390_1_%e7%ae%a1%e7%90%86%e7%90%86%e8%ae%ba%e5%af%bc%e8%ae%ba_0.25",
    "0100430_0_%e4%bc%9a%e8%ae%a1%e5%ad%a6%e5%af%bc%e8%ae%ba_0.5",
    "0100430_1_%e4%bc%9a%e8%ae%a1%e5%ad%a6%e5%af%bc%e8%ae%ba_0.5",
    "0100330_0_%e7%bb%8f%e6%b5%8e%e5%ad%a6%e5%af%bc%e8%ae%ba_0.25",
    "0100470_0_%e4%ba%ba%e5%8a%9b%e8%b5%84%e6%ba%90%e7%ae%a1%e7%90%86%e5%af%bc%e8%ae%ba_0.25",
    "0100440_0_%e7%a8%8e%e6%94%b6%e5%ad%a6%e5%af%bc%e8%ae%ba_0.25",
    "0100440_1_%e7%a8%8e%e6%94%b6%e5%ad%a6%e5%af%bc%e8%ae%ba_0.25",
    "0100460_0_%e7%89%a9%e6%b5%81%e7%ae%a1%e7%90%86%e5%af%bc%e8%ae%ba_0.25"
]

# Cookie="""ASP.NET_SessionId=jdmcmcirnxpui355epnt3kry; 3113003893=STINFO=3113003893%7c%e9%99%88%e9%be%99%7c%e7%94%b7%7c2013%7c%e7%94%b5%e5%ad%90%e4%bf%a1%e6%81%af%e5%b7%a5%e7%a8%8b(%e4%bf%a1%e6%81%af%e5%ae%89%e5%85%a8)%7c130807%7c130807%7c8%7c28%7c%7c06&ULIMIT=28&CET=0400303$0400320$0400342$0400351$0400430$0400470$0400440$0401650$0401690$0401720$0401730$0401740$0401750$0401630$0401640&DEZY=&ZXXK=; 3113003893_XZKC=XZKC=0300410_0_%e6%95%99%e5%b8%88%e5%8f%a3%e8%af%ad_0.5"""
# Cookie2="""ASP.NET_SessionId=jdmcmcirnxpui355epnt3kry;3113003893=STINFO=3113003893%7c%e9%99%88%e9%be%99%7c%e7%94%b7%7c2013%7c%e7%94%b5%e5%ad%90%e4%bf%a1%e6%81%af%e5%b7%a5%e7%a8%8b(%e4%bf%a1%e6%81%af%e5%ae%89%e5%85%a8)%7c130807%7c130807%7c8%7c28%7c%7c06&ULIMIT=28&CET=0400303$0400320$0400342$0400351$0400430$0400470$0400440$0401650$0401690$0401720$0401730$0401740$0401750$0401630$0401640&DEZY=&ZXXK=; 3113003893_XZKC=XZKC=0300410_0_%e6%95%99%e5%b8%88%e5%8f%a3%e8%af%ad_0.5"""
# Cookie3="""ASP.NET_SessionId=jdmcmcirnxpui355epnt3kry; 3113003893=STINFO=3113003893%7c%e9%99%88%e9%be%99%7c%e7%94%b7%7c2013%7c%e7%94%b5%e5%ad%90%e4%bf%a1%e6%81%af%e5%b7%a5%e7%a8%8b(%e4%bf%a1%e6%81%af%e5%ae%89%e5%85%a8)%7c130807%7c130807%7c8%7c28%7c%7c06&ULIMIT=28&CET=0400303$0400320$0400342$0400351$0400430$0400470$0400440$0401650$0401690$0401720$0401730$0401740$0401750$0401630$0401640&DEZY=&ZXXK=; 3113003893_XZKC=XZKC=0200230_2_%e7%94%9f%e5%91%bd%e6%95%99%e8%82%b2_0.5"""
while True:
     for cast in jingguan:
         Cookie = """ASP.NET_SessionId=jdmcmcirnxpui355epnt3kry; 3113003893=STINFO=3113003893%7c%e9%99%88%e9%be%99%7c%e7%94%b7%7c2013%7c%e7%94%b5%e5%ad%90%e4%bf%a1%e6%81%af%e5%b7%a5%e7%a8%8b(%e4%bf%a1%e6%81%af%e5%ae%89%e5%85%a8)%7c130807%7c130807%7c8%7c28%7c%7c06&ULIMIT=28&CET=0400303$0400320$0400342$0400351$0400430$0400470$0400440$0401650$0401690$0401720$0401730$0401740$0401750$0401630$0401640&DEZY=&ZXXK=; 3113003893_XZKC=XZKC=""" + cast
         headers = {
            "User-agent":User_agent,
            "Referer":Refere,
            "Cookie":Cookie
         }
         values ={
            # "__VIEWSTATE":"/wEPDwUIMjczNjAxNzUPZBYCAgMPZBYCAgMPZBYCAgEPZBYGZg8PFgIeBFRleHQFCTAzMDA0MjBfM2RkAgEPDxYCHwAFCeWPo+aJjeWtpmRkAgIPDxYCHwAFAzAuNWRkZKTF4DfxRaba0KNWAIXZsbnijlZL",
            # "__VIEWSTATEGENERATOR":"1D48D657",
            # "__EVENTVALIDATION":"/wEWAgKq1/3gBgKM54rGBqcjNmloBijE3gMkwBCguYcjeibv",
            "Button1":"确定选课"
            }
         data = urllib.urlencode(values)
         requset  = urllib2.Request(url=TskUrl,data=data,headers=headers)
         response = urllib2.urlopen(requset)
         print response.read()