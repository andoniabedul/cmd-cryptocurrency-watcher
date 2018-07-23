import json
#from helpers.format_response import exchanges as format_response
from helpers.messages import messages as messages
from api.call import exchanges as api_call 
class Ticket:
  def __init__(self, base_pair, pair):
    self.base_pair = base_pair
    self.pair = pair
    self.exchanges = ['coinbase', 'bitfinex', 'poloniex', 'gemini']

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
      formated_pairs = self.format_pairs(self.base_pair, self.pair, exchange)
      return url.format(formated_pairs)
  
  def get_pairs(self):
    return '{}{}'.format(self.base_pair, self.pair)
  
  def format_pairs(self, base_pair, pair, exchange):
    if exchange is 'bitfinex':
      return '{}{}'.format(base_pair, pair)
    if exchange is 'poloniex':
      return '{}_{}'.format(base_pair, pair)
    if exchange is 'coinbase':
      return '{}-{}'.format(base_pair.upper(), pair.upper())
    if exchange is 'gemini':
      return '{}{}'.format(base_pair, pair)
  
  @staticmethod
  def get(ticket):
    response_list = []
    for exchange in ticket.exchanges:
      pairs = ticket.format_pairs(ticket.base_pair, ticket.pair, exchange)
      if ticket.valid_pair(exchange):
        response = ticket.get_data(exchange, pairs)
        if response['success']:
          formated_response = messages['responses']['success'](response['data'], exchange)
          response_list.append(formated_response)
        else:
          formated_response = messages['responses']['error'](response['error'], exchange)
          response_list.append(formated_response) 
      else:
        formated_response = messages['responses']['invalid_pair'](ticket.get_pairs(), exchange)
        response_list.append(formated_response) 
    return response_list


  def get_data(self, exchange, pairs):
    url = self.get_url(exchange)
    response = api_call[exchange](url, pairs)
    if not hasattr(response, 'error'):
      return {
        'success': True,
        'data': response
      }
    else:
      return {
        'error': response['error']
      }
      
    


    

