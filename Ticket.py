import requests
import json
from helpers.format_response import exchanges as format_response

class Ticket:
  def __init__(self, base_pair, pair):
    self.base_pair = base_pair
    self.pair = pair
    self.exchanges = ['bitfinex']

  def valid_pair(self, exchange):
     with open('./constants/pairs_by_exchange.json') as pairs:
      pairs_exchange = json.load(pairs)[exchange]
      if self.base_pair in pairs_exchange:
        if self.pair in pairs_exchange[self.base_pair]:
          return True
      return False

  def get_url(self, exchange):
    with open('./constants/urls.json') as urls:
      tickets_url = json.load(urls)
      url = tickets_url['tickets'][exchange]
      return url
    
  def get(self):
    url = self.get_url(self.exchanges[0])
    if self.valid_pair('bitfinex'):
      api_response = requests.get(url.format(self.base_pair + self.pair))
      data = format_response['bitfinex'](api_response.json())
      return {
        'success': True,
        'exchange': self.exchanges[0],
        'data': data
      }
    else:
      return {
        'success': False,
        'data': 'Not valid pair/currency'
      }


    

