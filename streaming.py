from slistener import SListener
import time, tweepy, sys

## authentication
CONSUMER_KEY = 'laNbHK9rHTSN3VDjGjxKzGVlS'
CONSUMER_SECRET = '75usGshLnyRxGBa1kmgIMHS2GDQrjBG3ENzuDqJ2poT6nDpwv5'
ACCESS_TOKEN = '120044061-y5OLv9WBCCy810uq2TD7q9GqdZ15KoAYmEfGbvVc'
ACCESS_TOKEN_SECRET = 'HaXtD7ZRZrKMMGPGglaeXGGCa7Dzw0HE3jZ1oZbRSE0qM'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api      = tweepy.API(auth_handler=auth)

def main():
    track = ['obama', 'trump']
    follow = []
    fstr = "lederp17"
    u = api.get_user("lederp17")
    follow.append(str(u.id))
    listen = SListener(api, 'myprefix')
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