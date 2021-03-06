import os

from domain_checker import domain_checker
from article_scrapers import download_data, bloomberg_article, fox_article
from azure_api import AzureAPI
from image_processing import clarifai_analysis

def main(url=None, article_parameters=None, heroku=False):
    
    if url is None and article_parameters is None:
        raise SystemError('Either an article URL or article HTML must be '
                          'provided to main.py, however, neither were given.')
    elif url and article_parameters:
        raise Warning('Both a URL and an article HTML were provided to '
                      'main.py. Only the URL will be used.')

    if url:
        # The article is also requrested from the url provided
        article_html = download_data(url=url)

        # The domain is checked against a static list of fake news sites
        domain_clean = domain_checker(url=url)
        domain = domain_clean[0]

        # All important article parameters are parsed from the website
        if domain == 'bloomberg.com':
            article_parameters = bloomberg_article(raw_html=article_html)
        elif domain == 'foxnews.com':
            article_parameters = fox_article(raw_html=article_html)
        else:
            raise SystemError('The Fake News Detector only works with '
                              'Bloomberg.com and foxnews.com articles.')
    else:
        # The domain is checked against a static list of fake news sites
        domain_clean = domain_checker(url=article_parameters['source'])
        domain = domain_clean[0]
    
    # The user is made aware immediately if the site is on the list
    if len(domain_clean) > 1:
        print('WARNING! The article provided is sourced from %s, which is known '
              'to provide %s articles.' % (domain, domain_clean[1]))
        
    # Load the API keys
    if heroku:
        keys = {
            'bing_spell_check': os.environ.get('bing_spell_check', None),
            'text_analytics': os.environ.get('text_analytics', None),
            'clarifai_id': os.environ.get('clarifai_id', None),
            'clarifai_secret': os.environ.get('clarifai_secret', None)
        }
    else:
        from key_store import key_store
        keys = key_store()
    
    # Have to encode the text with utf8 to prevent encoding errors
    try:
        article_parameters['text'] = str(article_parameters['text']).encode('utf8')
    except Exception as e:
        print('Uknown error processing article in main')
        article_parameters['spelling'] = 0
        article_parameters['sentiment'] = 3
        article_parameters['image_tag_1'] = ''
        article_parameters['image_tag_2'] = ''
        article_parameters['image_tag_3'] = ''
        return article_parameters
    
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
        article_parameters['image_tag_%s' % str(int(i) + 1)] = concept
    
    # All the features are then passed to a ML model where it tries to identify fake articles
    
    # The results are sent back to the user with a short explanation
    return article_parameters


if __name__ == '__main__':

    test_url = 'https://www.bloomberg.com/news/articles/2017-06-23/senate-holdouts-seek-upper-hand-in-perilous-health-bill-talks'
    results = main(url=test_url)

    print(results)
