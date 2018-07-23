def success(data, exchange):
  return {
    success: True,
    exchange: exchange,
    data: data
  }

def error(error, exchange):
  return {
    success: False,
    exchange: exchange,
    error: error
  }

def invalid_pair(pairs, exchange):
  return {
    success: False,
    exchange: ticket.exchanges[0],
    error: 'Not valid pair/currency'
  }

responses = {
  'success': success,
  'error': error,
  'invalid_pair': invalid_pair
}