# Ecosia Search

A simple program that searches [Ecosia](https://www.ecosia.org) for random search terms.
The search terms are generated from a list of english nouns. <br>
By default the requests are send through servers of the Onion Network (TOR) using the TorRequest package.

## Ecosia.py
Ecosia Search (through TOR nodes).
  Using tor is the standard mode, but it needs some extra configuration, in order to work
  on your machine. See these links for the configuration and possible errors:
  - https://www.scrapehero.com/make-anonymous-requests-using-tor-python/
  - https://stackoverflow.com/questions/49470261/tor-failing-to-run-with-failed-to-bind-one-of-the-listener-ports


Further explanation is provided in each file, like:
  ```python
if self.isTor:
      # this password needs to be set in your .env file
      # simply create a new file and paste the password you set
      # while configuring tor. Make sure that the .env file is
      # in the same dir as the .config file
      self.tr = TorRequest(password=TOR_PASS)
```

## requestHeaderGenerator.py
This is used if a user decides to search without TOR to avoid/delay blocking. <br>
It generates a random request header: a random user agent and language.
- User agents are taken from:  https://udger.com/resources/ua-list <br>
- Current languages are: `['en-US,en', 'de-DE,de', 'en-GB,en', 'fr-FR,fr']`

## searchTermGenerator.py
Returns random combination of 1 to 3 nouns of the english language.<br>
Nounlist taken from http://www.desiquintans.com/nounlist



## Example usage

```python
from ecosiaSearchPerformer import ecosia as e

# == standard init == #
ecosia = e.Ecosia()

# perform the search
ecosia.search()
```
Output looks like:
> Performed request to url: https://www.ecosia.org/search?q=foal, <br>
> Got status code: 200

```python
# == init without using tor == #
ecosia = e.Ecosia(isTor=False)

# perform the search
ecosia.search()
```
Output looks like:
> Tor Option disabled <br>
> Performed request to url: https://www.ecosia.org/search?q=navigation, <br>
> Got status code: 200

## Requirements
```
certifi==2019.11.28
chardet==3.0.4
idna==2.8
numpy==1.18.1
pkg-resources==0.0.0
PySocks==1.7.1
python-dotenv==0.10.5
requests==2.22.0
stem==1.8.0
torrequest==0.1.0
urllib3==1.25.8
```

## Disclaimer
The project and the corresponding source code serve solely for the interest and illustration of the technical possibilities.
I assume no liability for any detrimental usage of the source code.
The mere presence/publication of this code on my Github account does not imply that I encourage scraping or scrape ecosia.org or any other website.
