def welcome():
  return """
    ####################################################
    ##                 Welcome to,                    ##
    ##                 CRYPTOWATCHER                  ##    
    ####################################################
  """

def console(response, pairs):
  return """
    → {exchange}
    → \x1b[1;33;40m{pairs} \x1b[0m
    → PRICE: \x1b[1;33;40m {price} \x1b[0m
    → AVERAGE PRICE: \x1b[1;36;40m{average}\x1b[0m

    → DAY HIGH: {high}
    → DAY LOW:  {low}

    → ASKS: \x1b[1;31;40m {ask} \x1b[0m     
    → BIDS: \x1b[1;32;40m {bid} \x1b[0m
    ______________________________
    {time}                                        
    
    """.format(
      price=response['data']['last'],
      pairs="".join(pairs),
      exchange=response['exchange'].upper(),
      average=response['data']['average'],
      high= response['data']['high'],
      low= response['data']['low'],
      ask= response['data']['ask'],
      bid= response['data']['bid'],
      time=response['data']['date']
    )

def console_multiple_out(response, pairs):
  return """
      → \x1b[1;33;40m{exchange}\x1b[0m | {pairs} 
      → PRICE:\x1b[1;33;40m {price} \x1b[0m
      → ASKS: \x1b[1;31;40m {ask} \x1b[0m |  BIDS: \x1b[1;32;40m {bid} \x1b[0m   
      ______________________
      {time}                                         
    """.format(
      price=float(response['data']['last']),
      pairs="".join(pairs),
      exchange=response['exchange'].upper(),
      average=response['data']['average'],
      high= response['data']['high'],
      low= response['data']['low'],
      ask= response['data']['ask'],
      bid= response['data']['bid'],
      time=response['data']['date']
    ) 

def success(data, exchange):
  return {
    'success': True,
    'exchange': exchange,
    'data': data
  }

def error(error, exchange):
  return {
    'success': False,
    'exchange': exchange,
    'error': error
  }

def invalid_pair(pairs, exchange):
  return {
    'success': False,
    'exchange': exchange,
    'error': 'Pair/currency not available on this exchange'
  }

messages = {
  'welcome': welcome(),
  'responses': {
    'console_multiple_out': console_multiple_out,
    'console': console,
    'success': success,
    'error': error,
    'invalid_pair': invalid_pair
  }
}