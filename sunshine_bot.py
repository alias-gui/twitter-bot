import tweepy
import time
from random import randint

from keys import *

#key.py contains keys (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#some random quotes, working on scraping these from the web somehow.

s0 = ' A dose of sunshine a day keeps the gloomy days away! \U0001F506'
s1 = ' Here is some sunshine for you! \U0001F506'
s2 = ' Did you call?! There is more than enough sunshine to go around! \U0001F506 I hope you have a good day!'
s3 = ' Here comes the sun, and some sunshine! \U0001F506 Keep smiling!'
s4 = ' Keep your face to the sun and you will never see the shadows. ― Helen Keller \U0001F506'
s5 = ' What sunshine is to flowers, smiles are to humanity. These are but trifles, to be sure; but scattered along life\'s pathway, the good they do is inconceivable. ― Joseph Addison \U0001F506'
s6 = ' Laughter is a sunbeam of the soul. ― Thomas Mann. Keep on laughing! \U0001F506'
s7 = ' After the rain, the sun will reappear. There is life. After the pain, the joy will still be here. ― Walt Disney Company \U0001F506'

l = [s0, s1, s2, s3, s4, s5, s6, s7]
#will randomise replies

def suns_reply():
    mentions = api.mentions_timeline(tweet_mode='extended')   
    with open('last_id.txt', 'r') as l_id:
        ls = []
        for line in l_id:
            line = line.strip()
            ls.append(line)
    
    for i in mentions:
        r = randint(0,len(l)-1)
        if '#sunshineplease' in i.full_text.lower():
            if str(i.id) not in ls:
                api.update_status('@'+i.user.screen_name+ ' ' +l[r]+ ' #SunshineBot #Python #100DaysofCode ', i.id)
                    with open('last_id.txt', 'a') as l_id:
                        l_id.write(str(i.id)+'\n')


if __name__ == '__main__':
    while True:
        suns_reply()
        time.sleep(120)
