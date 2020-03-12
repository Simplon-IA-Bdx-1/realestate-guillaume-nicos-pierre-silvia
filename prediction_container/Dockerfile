FROM python:3.7

USER predictor
# Changement du repertoire courant
WORKDIR /predictor

COPY ../models /predictor
RUN pip install -r requirements.txt
RUN pip freeze
#COPY /usr/ /usr/bin/flask/flask.py 




