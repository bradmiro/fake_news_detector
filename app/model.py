from sklearn.feature_extraction.text import TfidfVectorizer
import time
import jsonlines

def bag_of_words(docs):
    """
    :param docs: A list of articles
    :return: A tuple containing a list of words and a matrix of word counts by document.
    """
    # vectorizer = CountVectorizer(ngram_range=(1,2), token_pattern=r'\b\w+\b')

    vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words=['and', 'to', 'the', 'of'])

    return vectorizer
    # bag = vectorizer.fit_transform(docs).toarray()
    #
    # words = vectorizer.get_feature_names()
    #
    #
    #
    # else:
    #     return (words, bag)



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