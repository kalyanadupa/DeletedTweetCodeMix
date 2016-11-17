import requests
import lxml.html
import os,sys   
import json
proxies = {
  'http': 'http://10.3.100.207:8080',
  'https': 'http://10.3.100.207:8080',
}

def isDeleted(link):
    try:
        hxs = lxml.html.document_fromstring(requests.get(link, proxies=proxies).content)
        tx = hxs.xpath('//*[@class="js-tweet-text-container"]/p/text()')
        hx = hxs.xpath('//*[@class="js-tweet-text-container"]/p/a/b/text()')
        if((len(tx) ==0) |(len(hx) == 0)):
            return True
        return False
    except Exception, e:
        return False
        pass
    

if __name__ == "__main__":
    ip_folder_path = "ipt"
    op_folder_path = "files"
    content = sys.argv[1]
    input_file = ip_folder_path+'/'+content
    fn = open(input_file)
    op_file = op_folder_path+'/'+content[:-5]+'_deleted.json'   
    try:
        with open(input_file) as f:
            for line in f:        
                data = json.loads(line)
                print 
                for x in data:
                    x = x.replace("u\"","\"").replace("u\'","\'")
                    link = "https://twitter.com/lederp17/status/" + str(x)
                    if(isDeleted(link)):
                        fo = open(op_file, "a")
                        dct = {} 
                        dct[x] = str(data[x]).replace("u\"","\"").replace("u\'","\'")
                        # print(dct[x],str(data[x]).replace("u\"","\"").replace("u\'","\'"))
                        r = json.dumps(dct)
                        fo.write(r)        
                        fo.close()                         
                    else:
                        print x,"Not Deleted"
                        # print(x,str(data[x]).replace("u\"","\"").replace("u\'","\'")) 
    except Exception, e:
        print(e)
        pass                   