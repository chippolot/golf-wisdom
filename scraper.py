#!/usr/bin/env python -tt
  
import urllib2
from lxml.html import fromstring
import sys
import time
  
urlprefix = "http://www.brainyquote.com/quotes/keywords/golf"
urlsuffix = ".html"
  
#709
for page in xrange(1, 35):
    try:
        #print "-> page {} of {}".format(page, 34)
        urlpage = "_"+str(page) if page > 1 else ""
        url = urlprefix + urlpage + urlsuffix
        req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
        response = urllib2.urlopen(req)

        html = response.read()
        dom = fromstring(html)
        sels = dom.xpath('//*[(@class = "bqQuoteLink")]//a')
        for review in sels:
            if review.text:
                print review.text.rstrip()
        sys.stdout.flush()
        time.sleep(1)
    except:
        continue