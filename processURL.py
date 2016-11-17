import requests
import lxml.html
from ttp import ttp
import urllib    
import tldextract
import os   


def classifyTweet(input_file):           
    with open(input_file) as f:
        for tweet in f:
            tweet = tweet.replace("\/","/")
            p = ttp.Parser()
            toPrint = ""
            toPrint += tweet[:-1]    
            try:
                r = p.parse(tweet.decode('utf-8')) #parses tweets and stores it in data structure
                for link in r.urls:
                    resp = urllib.urlopen(link) #expands the t.co urls to normal urls
                    rx = requests.get(resp.url) #get the response code while opening the url 
                    #if the response code is 200 then the url is working
                    if(rx.status_code == requests.codes.ok):
                        if("twitter.com" in resp.url):
                            if(("/status/" in resp.url) & ("/photo/" in resp.url)): #checks if pic and text are present
                                hxs = lxml.html.document_fromstring(requests.get(resp.url).content)
                                tx = hxs.xpath('//*[@class="js-tweet-text-container"]/p/text()')
                                hx = hxs.xpath('//*[@class="js-tweet-text-container"]/p/a/b/text()')
                                ret = "";
                                idx = 0;
                                for xp in tx:
                                    if(xp != ""):
                                        ret += xp
                                        ret += " " 
                                    else:
                                        ret += hx[idx]
                                        idx = idx+1    
                                        ret += " "
                                ret = ret.strip()
                                toPrint += "|||"
                                toPrint += ret
                                toPrint += "||| Text + Pic"
                            else:
                                if("/status/" in resp.url):
                                    hxs = lxml.html.document_fromstring(requests.get(resp.url).content)
                                    tx = hxs.xpath('//*[@class="js-tweet-text-container"]/p/text()')
                                    hx = hxs.xpath('//*[@class="js-tweet-text-container"]/p/a/b/text()')
                                    ret = "";
                                    idx = 0;
                                    for xp in tx:
                                        if(xp != ""):
                                            ret += xp
                                            ret += " " 
                                        else:
                                            ret += hx[idx]
                                            idx = idx+1    
                                            ret += " "
                                    ret = ret.strip()
                                    toPrint += "|||"
                                    toPrint += ret
                        else:
                            hxs = lxml.html.document_fromstring(requests.get(resp.url).content)
                            sourceCode = lxml.html.tostring(hxs)
                            sub = "<img"
                            imgCount = sourceCode.count(sub,0,len(sourceCode))
                            toPrint += "|||image Count {}".format(imgCount)
            except Exception as e:
                print(str(e))
                pass
            print(toPrint)                


if __name__ == "__main__":
    folder_path = "new1"
    for content in os.listdir(folder_path):
        classifyTweet(folder_path+'/'+content)