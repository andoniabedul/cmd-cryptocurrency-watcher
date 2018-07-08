def welcome():
  return """
    ####################################################
    ##                 Welcome to,                    ##
    ##                 CRYPTOWATCHER                  ##    
    ####################################################
  """

def out_response(response, pairs):
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

messages = {
  'welcome': welcome(),
  'out_data': out_response
}