# from slistener import SListener
import time, tweepy, sys
import os

## authentication
CONSUMER_KEY = 'laNbHK9rHTSN3VDjGjxKzGVlS'
CONSUMER_SECRET = '75usGshLnyRxGBa1kmgIMHS2GDQrjBG3ENzuDqJ2poT6nDpwv5'
ACCESS_TOKEN = '120044061-y5OLv9WBCCy810uq2TD7q9GqdZ15KoAYmEfGbvVc'
ACCESS_TOKEN_SECRET = 'HaXtD7ZRZrKMMGPGglaeXGGCa7Dzw0HE3jZ1oZbRSE0qM'
fno = 0
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api      = tweepy.API(auth_handler=auth)

def main():
    follow = []
    ip_folder_path = "authors"
    flw  = open('userid/'+str(fno) + '.txt', 'w')
    for content in os.listdir(ip_folder_path):
        try:
            if ".txt" in content:
                fileNo = int(content[:-4])
                if fileNo%10 == fno:
                    print fileNo, "Done"
                    input_file = ip_folder_path+'/'+content
                    with open(input_file) as f:
                        for line in f:
                            try:
                                # print line
                                u = api.get_user(line)
                                follow.append(str(u.id))
                                flw.write(str(u.id)+'\n')
                            except Exception as e:
                                print "error 1 ! ", str(e)
                                # print line
                                pass                        
        except Exception as e:
            print "error 2 ! ", str(e)
            pass
    flw.close()
    print "Write Done"
    listen = SListener(api, str(fno))
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."
    while(1):
        try: 
            stream.filter(follow = follow)
        except Exception as e:
            print "error!", str(e)
            pass

if __name__ == '__main__':
    main()