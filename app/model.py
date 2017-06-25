from sklearn.feature_extraction.text import TfidfVectorizer


def bag_of_words():
    """
    This will return a TfidfVectorizer object to build a bag of words.

    :return: A tuple containing a list of words and a matrix of word counts by document.
    """
    return TfidfVectorizer(max_features=5000, sublinear_tf=True, stop_words=['and', 'to', 'the', 'of'])


class BOWModel:
    """
    This is a class that will build a model suitable for making predictions comparing bodies
    of text. Specifically, the Bag of Words method will be implemented.

    An sklearn regression model object is needed to initialize this model.
    """

    y_ = None

    def __init__(self, model):
        """Initializes the model.

        :params model: An sk-learn model object.
        """
        self.model = model
        self.vectorizer = bag_of_words()

    def fit(self, input_, y):
        """Fits the model using a Bag of Words.

        :param input_: A list of bodies of text data to train a bag of words.
        :param y: The training target values corresponding to the input text data.
        """
        bag = self.vectorizer.fit_transform(input_).toarray()
        self.model.fit(X=bag, y=y)

    def predict(self, input_):
        """Makes a prediction given some test data.

        :param input_: This is the data to make a prediction off of.

        :returns: A np array with prediction values.
        """
        new_bag = self.vectorizer.transform(input_)
        self.y_ = self.model.predict(new_bag)
        return self.y_

    def error(self, y, threshold=0.05):
        """Calculates the error of the model prediction. Since this model is
        trained using a regressor, we include a threshold to depict whether or not
        both the actual data and the prediction data fall on the same side of the
        threshold. A prediction is counted as a hit if they do, and a miss otherwise.

        :param y: The actual y values to compare to.
        :param threshold: The threshold for which we should test data. Default is 0.05.

        :returns: The error percentage of our test data.
        """
        error_count = 0

        for i in range(len(y)):
            if (y[i] < threshold < self.y_[i]) or (y[i] > threshold > self.y_[i]):
                error_count += 1

        self.error = float(error_count)/len(y)

        print("Error for threshold of {}: {}".format(threshold, self.error))

        return self.error