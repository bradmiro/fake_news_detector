import os

from domain_checker import domain_checker
from article_scrapers import download_data, bloomberg_article, fox_article
from key_store import key_store
from azure_api import AzureAPI
from image_processing import clarifai_analysis

dir = os.path.dirname(__file__)

# User submits a url (from a pre-approved source) they want to check
url = 'https://www.bloomberg.com/news/articles/2017-06-23/senate-holdouts-seek-upper-hand-in-perilous-health-bill-talks'

# The domain is checked against a static list of fake news sites
domain_clean = domain_checker(url=url)
domain = domain_clean[0]

# The user is made aware immediately if the site is on the list
if len(domain_clean) > 1:
    print('WARNING! The article provided is sourced from %s, which is known '
          'to provide %s articles.' % (domain, domain_clean[1]))

# The article is also requrested from the url provided
article_html = download_data(url=url)

# All important article parameters are parsed from the website
if domain == 'bloomberg.com':
    article_parameters = bloomberg_article(raw_html=article_html)
elif domain == 'foxnews.com':
    article_parameters = fox_article(raw_html=article_html)
else:
    raise SystemError('The Fake News Detector only works with Bloomberg.com '
                      'and foxnews.com articles.')

# Load the API keys
keys = key_store()

# Send the article text to Azure Cognitive Service API for analysis
azure_api = AzureAPI(keys=keys, article_params=article_parameters)
# Calculate the spelling accuracy for the article text
spelling_score = azure_api.bing_spell_check()
article_parameters['spelling'] = spelling_score
# Calculate the sentiment scores for each sentence in the article
sentiment_scores = azure_api.text_analytics()
article_parameters['sentiment'] = sentiment_scores

# Send the article image to clairifai for topic processing
image_top_concepts = clarifai_analysis(img_path=article_parameters['image'],
        keys=keys, n=3)
for i, concept in enumerate(image_top_concepts):
    # Create paramters ('image_tag_1') for each n concepts
    article_parameters['image_tag_%s' % i] = concept

print(article_parameters)

# All the features are then passed to a ML model where it tries to identify fake articles

# The results are sent back to the user with a short explanation
