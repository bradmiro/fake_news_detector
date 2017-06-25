import os

from domain_checker import domain_checker

dir = os.path.dirname(__file__)

# User submits a url (from a pre-approved source) they want to check
url = 'https://www.bloomberg.com/news/articles/2017-06-23/senate-holdouts-seek-upper-hand-in-perilous-health-bill-talks'

# The domain is checked against a static list of fake news sites
domain_clean = domain_checker(url=url)

# The user is made aware immediately if the site is on the list
if not domain_clean:
    print('WARNING! The article provided is sourced from %s, which is known '
          'to provide %s articles.' % (domain_clean[0], domain_clean[1]))

# The article is also requrested from the url provided

# All important article parameters are parsed from the website

# Some paraemters are sent to the Azure API and clarifai API to get more features

# All the features are then passed to a ML model where it tries to identify fake articles

# The results are sent back to the user with a short explanation
