import pandas as pd

"""This file will take as input a dictionary with the following schema:

source: Source domain (domain.com)
author: The author, if provided
title: The title of the article
text: The text of the article
image_tag_1: The highest rated tag from the Clarifai API
image_tag_2: The 2nd highest rated tag from the Clarifai API
image_tag_3: The 3rd highest rated tag from the Clarifai API
spelling: 1 if 3+ spelling errors are identified from Azure, 0 otherwise
sentiment: 1-5, 1 being very negative, 5 being very positive

Output schema (list):

source - string
author - string
image_tag_1 - string
image_tag_2 - string
image_tag_3 - string
spelling - binary int (0,1)
sentiment_1 - binary int (0,1)
sentiment_2 - binary int (0,1)
sentiment_3 - binary int (0,1)
sentiment_4 - binary int (0,1)
title - text 
text - text
target (optional) - float
"""

def pickle_load():
    """Load bag of words parameters from pickled file.

     :returns: A np array of weights
     """
    pass

def preprocess(data_dict):

    data = []

    data.append(data_dict['source'])
    data.append(data_dict['author'])
    data.append(data_dict['image_tag_1'])
    data.append(data_dict['image_tag_2'])
    data.append(data_dict['image_tag_3'])
    data.append(data_dict['spelling'])

    sentiment = int(data_dict['sentiment'])

    for i in range(1,5):
        data.append(1 if i == sentiment else 0)

    data.append(data_dict('title'))
    data.append(data_dict('text'))

    if 'target' in data_dict:
        data.append(data_dict['target'])

    return data