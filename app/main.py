# User submits a url (from a pre-approved source) they want to check

# The domain is checked against a static list of fake news sites

# The user is made aware immediately if the site is on the list

# The article is also requrested from the url provided

# All important article parameters are parsed from the website

# Some paraemters are sent to the Azure API and clarifai API to get more features

# All the features are then passed to a ML model where it tries to identify fake articles

# The results are sent back to the user with a short explanation
