FROM heroku/miniconda

# Grab requirements.txt
ADD ./app/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install -qr /tmp/requirements.txt

# Add the app code
ADD ./app /opt/app/
WORKDIR /opt/app

RUN conda install scikit-learn

CMD gunicorn --bind 0.0.0.0:$PORT wsgi
