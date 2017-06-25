from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import time
import jsonlines

def bag_of_words():
    """
    This will return a TfidfVectorizer object to build a bag of words.

    :return: A tuple containing a list of words and a matrix of word counts by document.
    """

    vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words=['and', 'to', 'the', 'of'])

    return vectorizer


class BOW_Model:
    """
    This is a class that will build a model suitable for making predictions comparing bodies
    of text. Specifically, the Bag of Words method will be implemented.

    An sklearn regression model object is needed to initialize this model.
    """

    def __init__(self, model):
        """Initializes the model.

        :params model: An sklearn regression model object.
        """
        self.model = model


    def fit(self, input, y):
        """Fits the model using a Bag of Words.

        :param input: A list of bodies of text data to train a bag of words.
        :param y: The training target values corresponding to the input text data.
        """

        self.vectorizer = bag_of_words()
        bag = self.vectorizer.fit_transform(input).toarray()
        self.model.fit(X=bag, y=y)

    def predict(self, X):
        """Makes a prediction given some test data.

        :param X: The input feature test data to make a prediction off of.

        :returns: A np array with prediction values.
        """
        new_bag = self.vectorizer.transform(X)
        self.y_ = self.model.predict(new_bag)
        return self.y_

    def error(self, y, threshold=0.05):
        """Calculates the error of the model prediction. Since this model is
        trained using a regressor, we include a threshold to depict whether or not
        both the actual data and the prediction data fall on the same side of the
        threshold. A prediction is counted as a hit if they do, and a miss otherwise.

        :param y: The actual y values to compare to.
        :threshold: The threshold for which we should test data. Default is 0.05.

        :returns: The error percentage of our test data.
        """
        error_count = 0

        for i in range(len(y)):
            if (y[i] < threshold < y_[i]) or (y[i] > threshold > y_[i]):
                error_count += 1

        self.error = float(self.error_count)/len(self.y)
        return self.error

        print ("Error for threshold of {}: {}".format(threshold, self.error))










if __name__ == '__main__':

    objs = []
    with open('/Users/bmirombp/ai_hack/fake_news_detector/data/signalmedia-1m.jsonl') as f:
        for obj in f:
            objs.append(obj)
    test = ['Print They should pay all the back all the money plus interest. The entire family and everyone who came in with them need to be deported asap. Why did it take two years to bust them? Here we go again …another group stealing from the government and taxpayers! A group of Somalis stole over four million in government benefits over just 10 months! We’ve reported on numerous cases like this one where the Muslim refugees/immigrants commit fraud by scamming our system…It’s way out of control! More Related',
            'Why Did Attorney General Loretta Lynch Plead The Fifth? Barracuda Brigade 2016-10-28 Print The administration is blocking congressional probe into cash payments to Iran. Of course she needs to plead the 5th. She either can’t recall, refuses to answer, or just plain deflects the question. Straight up corruption at its finest! 100percentfedUp.com ; Talk about covering your ass! Loretta Lynch did just that when she plead the Fifth to avoid incriminating herself over payments to Iran…Corrupt to the core! Attorney General Loretta Lynch is declining to comply with an investigation by leading members of Congress about the Obama administration’s secret efforts to send Iran $1.7 billion in cash earlier this year, prompting accusations that Lynch has “pleaded the Fifth” Amendment to avoid incriminating herself over these payments, according to lawmakers and communications exclusively obtained by the Washington Free Beacon. Sen. Marco Rubio (R., Fla.) and Rep. Mike Pompeo (R., Kan.) initially presented Lynch in October with a series of questions about how the cash payment to Iran was approved and delivered. In an Oct. 24 response, Assistant Attorney General Peter Kadzik responded on Lynch’s behalf, refusing to answer the questions and informing the lawmakers that they are barred from publicly disclosing any details about the cash payment, which was bound up in a ransom deal aimed at freeing several American hostages from Iran. The response from the attorney general’s office is “unacceptable” and provides evidence that Lynch has chosen to “essentially plead the fifth and refuse to respond to inquiries regarding [her]role in providing cash to the world’s foremost state sponsor of terrorism,” Rubio and Pompeo wrote on Friday in a follow-up letter to Lynch. More Related',
            'Email Kayla Mueller was a prisoner and tortured by ISIS while no chance of release…a horrific story. Her father gave a pin drop speech that was so heartfelt you want to give him a hug. Carl Mueller believes Donald Trump will be a great president…Epic speech! 9.0K shares']

    start = time.time()
    w, b = bag_of_words(test, tfidf=True)
    end = time.time()


    print (b)
    print ("Length of bag:", len(b[0]))
    print (end-start)