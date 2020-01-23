
from ecosiaSearchPerformer import ecosia as e

# == standard init == #
ecosia = e.Ecosia()

# perform the search
ecosia.search()

# Output looks like:
# > Performed request to url: https://www.ecosia.org/search?q=foal,
# Got status code: 200

# == init without using tor == #
ecosia = e.Ecosia(isTor=False)

# perform the search
ecosia.search()

# Output looks like:
# > Tor Option disabled
# > Performed request to url: https://www.ecosia.org/search?q=navigation,
# Got status code: 200
