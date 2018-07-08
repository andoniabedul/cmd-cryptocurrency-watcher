import sys
from services.Ticket import Ticket
from colorama import Style, Fore
from helpers.messages import messages as messages


def welcome():
  return """
    ####################################################
    ##                 Welcome to,                    ##
    ##                 CRYPTOWATCHER                  ##    
    ####################################################
  """

def get_info():
  commands = sys.argv
  if len(commands) <= 1:
    pair = input("Enter the pair that you wanna watch: ")
    base_pair = input("Enter your currency: ")
  else:
    pair = commands[1].strip().upper()
    base_pair = commands[2].strip().upper()
  return [pair, base_pair]

def init():
  print(messages['welcome'])
  pairs = get_info()
  ticket = Ticket(pairs[0], pairs[1])
  response = ticket.get()
  
  if response['success']:
    print(
      messages['out_data'](response, pairs)
    )
  else:
    print(
      response['data']
    )
  
  

init()