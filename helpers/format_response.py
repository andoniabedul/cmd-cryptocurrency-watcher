from jsonschema import validate as isValid
import time 
import sys

response_schema = {
    "type" : "object",
    "properties" : {
        "exchange":{"type": "string"},
        "average" :{"type": "string"},
        "high"    :{"type": "string"},
        "low"     :{"type": "string"},
        "ask"     :{"type": "string"},
        "bid"     :{"type": "string"},
        "last"    :{"type": "string"},
        "date"    :{"type": "string"}
    },
}
def bitfinex(res):
  data = {
    "average" : res['mid'],
    "high"    : res['high'],
    "low"     : res['low'],
    "ask"     : res['ask'],
    "bid"     : res['bid'],
    "last"    : res['last_price'],
    "date"    : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(res['timestamp']))) 
  }
  validation = isValid(res, response_schema)
  if validation is not Exception:
    return data


exchanges = {
  'bitfinex': bitfinex
}

