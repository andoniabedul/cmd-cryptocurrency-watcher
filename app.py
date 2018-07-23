import sys
from services.Ticket import Ticket
from helpers.messages import messages as messages


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
  responses = Ticket.get(ticket)
  formated_responses = [ticket for ticket in responses if ticket['success'] is True]
  ticket_errors = [ticket for ticket in responses if ticket['success'] is False]
  for response in formated_responses:
    print(
        messages['responses']['console_multiple_out'](response, pairs)
      )
  for ticket_error in ticket_errors:
    print("* {}: {}".format(ticket_error['exchange'].upper(), ticket_error['error']))
  
  

init()