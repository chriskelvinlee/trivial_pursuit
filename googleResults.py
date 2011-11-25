# Author: Michael Chen
# Date: 11/17/11
# Returns a list with links in order that they appear in Google search
# Warning: Might not handle symbols in queries well
# TODO: Filter out youtube, etc? idk
# TODO: Options: Filter, etc.
# TODO: Eventually let's just use google API

import urllib2
import re

def getGoogleLinks(query, pages = 1):
    links = []

    # Build request information:
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    query = query.lstrip().rstrip()
    query = re.sub('[ ]+', '+', query)
    base = "http://www.google.com/search?q=" + query

    for i in range(0, pages):
        # Get full page source
        url = base + "&start=" + str(i * 10)
        req = urllib2.Request(url,None,headers)
        f = urllib2.urlopen(req)
        source = f.read()

        # Cut out garbage
        source = source.partition("id=\"search\"")[2]
        source = source.partition("id=\"botstuff\"")[0]

        # Get external links (not Google's)
        l = re.findall("class=\"r\"><a href=\"(http://[^\"]*)",source)
        for link in l:
            links.append(link)
    return links
