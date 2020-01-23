
import os
import random
import numpy as np
from os.path import join, dirname

class SearchTermGenerator:
    """
    SearchTermGenerator:
    Returns random combination of 1 to 3 nouns of the english language.
    Nounlist taken from
    > http://www.desiquintans.com/nounlist
    """
    def __init__(self):
        self.nounListFile = join(dirname(__file__), 'files/nounlist.txt')
        self.nounsAmountMax = 3

    def getSearchTerm(self):
        nouns = []
        try:
            with open(self.nounListFile) as f:
                lines = f.readlines()
                if len(lines) > 0:
                    nounsAmount = random.randint(1,self.nounsAmountMax)
                    prng = np.random.RandomState()
                    index = prng.permutation(len(lines) - 1)
                    idxs = list(np.asarray(index, dtype=np.integer))[:nounsAmount]
                    for i in idxs:
                        nouns.append(lines[int(i)].replace("\n",""))
        except Exception as err:
            print('Exception in _readTerms')
            print(str(err))
        finally:
            return nouns
