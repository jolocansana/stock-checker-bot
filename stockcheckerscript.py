import requests
import json
import schedule
import time
from urllib.parse import quote

HEADERS = {
    'Host': 'www.bloomberg.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Accept': '*/*',
    'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.bloomberg.com/quote/',
    'DNT': '1',
    'Connection': 'keep-alive',
    'TE': 'Trailers'
}
URL="https://www.bloomberg.com/markets2/api/datastrip"
URL_PARAMS = 'locale=en&customTickerList=true'

object_append = '%s:%s' % ('ALFMGIF', 'PM')
headers = HEADERS
headers['Referer'] += object_append

def send():
  url = '%s/%s?%s' % (URL, quote(object_append), URL_PARAMS)
  response = requests.get(url=url, headers=headers)
    
  if response.status_code in range(200, 230):
    price = response.json()[0]['price']

  bot_token = "5032499965:AAG-hEC0UKz22luV6wEPC_3pEZd7rYYhQn4"
  bot_chatID = "671015453"
  bot_message = "ALFMGIF current price is {}".format(price)
  send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
  response = requests.get(send_text)

schedule.every().hour.do(send)

while True:
  schedule.run_pending()
  time.sleep(1)