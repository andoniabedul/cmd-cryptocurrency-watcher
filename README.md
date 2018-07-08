## Synopsis

Project to keeping track of cryptocurrencies on several exchanges from command line. 

## Code Example
On Python: 3.6

**Services**: Here is the classes for manage the behavior of differents services that the exchanges provides:
  -Tickets
  -Orders book
  -Trades

For the moment it's only developed the Ticket class and it's harcoded for Bitfinex. 

**Helpers**:
  - messages.py: All the messages that it's printed out on the application.
  - format_response.py: All the logic for manage the response of the exchanges.

**Constants**:
  - pairs_by_exchange.json: All exchanges with all pairs at the moment, to validate if the exchange have the pair.
  - urls.json: All the URL's for the differents services that exchanges provides.

## Examples of use

from command line: python3.6 app.py btc usd

## License

A short snippet describing the license (MIT, Apache, etc.)
