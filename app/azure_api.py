import json

import http.client
import urllib.request
import urllib.parse
import urllib.error

from nltk import tokenize


class AzureAPI:

    def __init__(self, keys, article_params):
        """
        :param keys: Dictionary of Azure API keys
        :param article_data: Dictionary of article parameters
        """
        self.keys = keys
        self.article_params = article_params

    def bing_spell_check(self):
        """Pass article text to Bing spell check. Calculate the percent
        of words that are misspelled from the whole."""
       
        headers = {
            # Request headers
            'Content-Type': 'application/x-www-form-urlencoded',
            'Ocp-Apim-Subscription-Key': self.keys['bing_spell_check'],
        }
        
        params = urllib.parse.urlencode({
            # Request parameters
            'mode': 'proof',
            'mkt': 'en-us',
        })
        
        raw_text = self.article_params['text']
        # Replace all spaces in the text with plus signs that Azure requires
        body = 'Text=' + raw_text.replace(' ', '+')
        
        try:
            conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
            conn.request("POST", "/bing/v5.0/spellcheck/?%s" %
			 params, body, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))

        data_dict = json.loads(data)
        spelling_error_perc = len(data_dict['flaggedTokens']) / len(raw_text.split())
        return spelling_error_perc

    def text_analytics(self):
        """Send the article text to the text analytics api where it will get
        a sentiment score. The article is broken down into sentences, where
        each sentence is given a sentiment score (Microsoft recommends this).

        https://www.johanahlen.info/en/2017/04/text-analytics-and-sentiment-analysis-with-microsoft-cognitive-services/

        :return: List of sentence sentiments
        """

        headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.keys['text_analytics'],
        }
        
        sentiment_url = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'
        
        raw_text = self.article_params['text']

        # Build post for sentiment
        sentences = tokenize.sent_tokenize(raw_text)
        content = []
        for i, sentence in enumerate(sentences):
            content.append({'id': str(i), 'language': 'en', 'text': sentence})
        body = json.dumps({"documents": content}).encode('utf-8')

        request = urllib.request.Request(sentiment_url, body, headers)
        response = urllib.request.urlopen(request)
        json_response = json.loads(response.read().decode('utf-8'))
            
        # Only return a list of the sentence sentiments
        return json_response['documents']


if __name__ == '__main__':

    from datetime import datetime
    from key_store import key_store

    test_keys = key_store()
    test_article = {
        'title': 'How to clean a build a brain',
        'date': datetime(2017, 6, 24),
        'source': 'HackerNews',
        'text': "Building a brain is hard. It requires lots of luck. Sometimes I thiink I now what I'm doing, but I atually don't."
    }

    api = AzureAPI(keys=test_keys, article_params=test_article)
    spelling_score = api.bing_spell_check()
    print(spelling_score)
    sentiments = api.text_analytics()
    print(sentiments)
