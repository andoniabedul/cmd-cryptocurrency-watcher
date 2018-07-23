import requests
from jsonschema import validate as isValid
import time 
import sys

schemas = {
  'bitfinex' : {
    'type' : 'object',
    'properties' : {
        'exchange':{'type': 'string'},
        'average' :{'type': 'string'},
        'high'    :{'type': 'string'},
        'low'     :{'type': 'string'},
        'ask'     :{'type': 'string'},
        'bid'     :{'type': 'string'},
        'last'    :{'type': 'string'},
        'date'    :{'type': 'string'}
    },
  },
  'poloniex': {
    'type': 'object',
    'properties': {
      'lowestAsk'     :{'type': 'string'},
      'highestBid'    :{'type': 'string'},
      'percentChange' :{'type': 'string'},
      'baseVolume'    :{'type': 'string'},
      'isFrozen'      :{'type': 'string'},
      'high24hr'      :{'type': 'string'},
      'low25hr'       :{'type': 'string'},
    }
  },
  'gemini': {
    'type': 'object',
    'properties': {
      'ask': {'type': 'string'},
      'bid': {'type': 'string'},
      'last': {'type': 'string'},
      'volume': {
          'type': 'object',
          'properties': {
            'BTC': {'type': 'string'},
            'USD': {'type': 'string'},
            'timestamp': {'type': 'integer'}
          } 
      }
    }
  },
  'coinbase':{
    'type': 'object',
    'properties': {
      'trade_id': {'type': 'integer'},
      'price'   : {'type': 'string'},
      'size'    : {'type': 'string'},
      'bid'     : {'type': 'string'},
      'ask'     : {'type': 'string'},
      'volume'  : {'type': 'string'},
      'time'    : {'type': 'string'}
    }
  }
}

def bitfinex(url, pairs):
  res = requests.get(url).json()
  validation = isValid(res, schemas['bitfinex'])
  if validation is not Exception:
    return {
      "average" : res['mid'],
      "high"    : res['high'],
      "low"     : res['low'],
      "ask"     : res['ask'],
      "bid"     : res['bid'],
      "last"    : res['last_price'],
      "date"    : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(res['timestamp']))) 
    }
  else:
    return {'error': str(res)}

def poloniex(url, pairs):
  res = requests.get(url).json()
  res = res[pairs]
  validation = isValid(res, schemas['poloniex'])
  if validation is not Exception:
    return {
      "average": (float(res['low24hr']) + float(res['high24hr'])) / 2,
      "high": res['high24hr'],
      "low": res['low24hr'],
      "ask": res['lowestAsk'],
      "bid": res['highestBid'],
      "last": res['last'],
      "date": time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    }
  else:
    return {'error': str(res)}
    

def coinbase(url, pairs):
  res = requests.get(url).json()
  validation = isValid(res, schemas['coinbase'])
  if validation is not Exception:
    return {
      "average": '0',
      "high": '0',
      "low": '0',
      "ask": res['ask'],
      "bid": res['bid'],
      "last": res['price'],
      "date": time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    }
  else:
    return {'error': str(res)}
  
def gemini(url, pairs):
  res = requests.get(url).json()
  validation = isValid(res, schemas['gemini'])
  if validation is not Exception:
    return {
      "average": '0',
      "high": '0',
      "low": '0',
      "ask": res['ask'],
      "bid": res['bid'],
      "last": res['last'],
      "date": time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    }
  else:
    return {'error': str(res)}

exchanges = {
  'bitfinex': bitfinex,
  'poloniex': poloniex,
  'coinbase': coinbase,
  'gemini': gemini
}

