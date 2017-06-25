import os
import pandas as pd
from urllib.parse import urlparse

def domain_checker(url):
    """
    :param url: Verify this URL from a loaded list of urls
    :return: True if domain is already flagged, False otherwise.
    """

    # Open the flagged source file in a pandas dataframe
    dir = os.path.dirname(__file__)
    flagged_source_file = os.path.join(dir, 'data', 'flagged_sources.csv')
    flagged_sources_df = pd.read_csv(flagged_source_file)

    # Parse the domain name out of the provided url
    parsed_url = urlparse(url)
    url_domain = '{uri.netloc}'.format(uri=parsed_url)
    url_domain = url_domain.replace('www.', '')

    if not url_domain:
        raise Warning('Unable to determine the root URL for the following '
                      'file in domain_checker: %s' % (url,))
        return None

    # Search the DF to see if the clean URL has a match
    flagged_row = flagged_sources_df.loc[flagged_sources_df['url'] == url_domain]

    if len(flagged_row) > 0:
        type_1 = flagged_row['type'].iloc[0]
        type_2 = flagged_row['2nd type'].iloc[0]
        if type_2 == 'nan':
            return [url_domain, type_1, type_2]
        else:
            return [url_domain, type_1]
    else:
        return [url_domain]


if __name__ == '__main__':
    test_url_1 = 'https://www.bloomberg.com/news/articles/2017-06-23/senate-holdouts-seek-upper-hand-in-perilous-health-bill-talks'
    test_url_2 = 'http://www.zerohedge.com/news/2017-06-24/bernie-sanders-wife-under-fbi-investigation-bank-fraud'
    test_url_3 = 'http://www.foxnews.com/politics/2017/06/24/trump-questions-why-obama-allegedly-did-nothing-about-russia-hacking-in-fox-interview.html'

    result_1 = domain_checker(test_url_1)
    result_2 = domain_checker(test_url_2)
    result_3 = domain_checker(test_url_3)

    print(result_1)
    print(result_2)
    print(result_3)
