# Fake News Detector

## Inspiration
We all get tired of seeing fake, misleading and click-bait articles. Why not have a service that can help you quickly identify articles that you should ignore?

## What it does
A user submits an article's URL[1] to our API (via the web app) and we analyze how accurate the article is based on actual content, images and metadata. Our analysis is provided back to the user so they know what they are potentially getting into.

[1]Currently we have the API limited to articles from Bloomberg and Fox News

## How we built it
The analysis pipeline is broken down into multiple steps. It starts by cross checking the source's domain against a database of fake news sites (satire, fake, etc.). The article's content is then scraped from the source, and we analyze the parameters. The main parameters used include spelling issues, the article's sentiment, the relationship between the title and the article text, and the image content (if provided). The spelling issues and article sentiment were derived from the Microsoft Azure APIs, and the image content classification was found from Clarifai's topic classification model. All parameters are then passed into a Support Gradient Descent Regressor to determine likelihood of being false.

## Challenges we ran into
As with all data from the internet, there were many data formatting and encoding issues. Building a working and reliable SGD regression was one of the largest challenges. Finally, building a working and stable web application was a sizable challenge.

## Accomplishments that we're proud of
We were able to pull together multiple API's to achieve the goal of our application. The pipeline was sturdy enough to handle both training and live data. Finally, the SGD model showed signs of very good accuracy with the data we provided it.

## What we learned
We became better with machine learning algorithms (Scikit-learn), and integrating multiple processes into a unified production application.

## What's next for Fake News Detector
To finalize the machine learning model, maybe exploring additional models that might improve the speed and accuracy. Also, we would really like to improve the web application, along with adding more ways for users to access the API.
