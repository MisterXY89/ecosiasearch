

import requests
from .config import *
import urllib.parse
from torrequest import TorRequest
from .requestHeaderGenerator import RequestHeaderGenerator
from .searchTermGenerator import SearchTermGenerator

class Ecosia:
    """
    Ecosia Search (through TOR nodes).
    Using tor is the standard mode, but it needs some extra config, in order to work
    on your machine. See these links for the config and possible errors:
    > https://www.scrapehero.com/make-anonymous-requests-using-tor-python/
    > https://stackoverflow.com/questions/49470261/tor-failing-to-run-with-failed-to-bind-one-of-the-listener-ports
    """
    def __init__(self, isTor = True):
        self.searchURL = "https://www.ecosia.org/search?q="
        # init generators
        self.rhGen = RequestHeaderGenerator()
        self.stGen = SearchTermGenerator()
        self.isTor = isTor
        if self.isTor:
            # this password needs to be set in your .env file
            # simply create a new file and paste the password you set
            # while configuring tor. Make sure that the .env file is
            # in the same dir as the .config file
            self.tr = TorRequest(password=TOR_PASS)

    def _buildUrl(self):
        """
        build search url with given search terms and make sure,
        that they are correctly encoded
        """
        return self.searchURL + "+".join(list(map(urllib.parse.quote, self.stGen.getSearchTerm())))

    def search(self):
        """
        requests ecosia search results page
        has 2 modes: anonymous reqs via tor or normal ones
        to avoid blocking for normal reqs I generate for every req a new req header
        """
        url = self._buildUrl()
        if self.isTor:
            self.tr.reset_identity()
            response = self.tr.get(url)
        else:
            print("Tor Option disabled")
            response = requests.get(url, headers = self.rhGen.getRandomRequestHeader())

        print(f"Performed request to url: {url}, \nGot status code: {response.status_code}")

        return response.status_code
