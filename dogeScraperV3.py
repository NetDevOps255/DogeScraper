from bs4 import BeautifulSoup
import requests
import time
from pushbullet import Pushbullet

API_KEY = 'o.miq9jvjygGKCx6BWZAJxU27j9ewHB5Xo'

pb = Pushbullet(API_KEY)

def doge_current():
    html_text = requests.get('https://nomics.com/assets/doge-dogecoin').text
    soup = BeautifulSoup(html_text, 'lxml')
    coin = soup.find('h1', class_ = 'fw5 f-30-s f2-l n-near-black ma0').text
    current_price = soup.find('span', class_ = 'mono f3 f-30-l fw5 n-near-black nowrap n-mb1-neg-l lh-solid').text
    current = float(current_price.strip('$'))
    percentage_change = soup.find('span', class_ = 'mono fw5 f4-l').text
    rank = soup.find('span', class_ = 'db mono f5').text
    #push = pb.push_note('Time to buy DOGE', 'Current Price is: ' + (current_price))
    while True:
        if current <= 0.37:
            return pb.push_note('Time to buy DOGE', 'Current Price is: ' + str(current))    

#    print(f'''
#Cryptocurrency: {coin}
#Current Price: {current_price}
#Percentage Change: {percentage_change}
#''')
'''
if __name__== '__main__':
    while True:
        doge_current()
        time_wait = 1
        print(f'Waiting {time_wait} minute....')
        time.sleep(time_wait * 60)
'''


doge_current()