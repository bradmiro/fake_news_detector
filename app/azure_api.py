import json

import http.client
import urllib.request
import urllib.parse
import urllib.error


class AzureAPI:

    def __init__(self, keys, article_params):
        """
        :param keys: Dictionary of Azure API keys
        :param article_data: Dictionary of article parameters
        """
        self.keys = keys
        self.article_params = article_params

    def bing_spell_check(self):
       
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
