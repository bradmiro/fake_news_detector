from flask import Flask, render_template, request

from main import main


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('website/interface.html')


@app.route('/', methods=['POST'])
def veryify_url():
    url = request.form['url']
    article_params = main(url=url, heroku=True)
    return article_params


if __name__ == '__main__':
    app.run(host='0.0.0.0')
