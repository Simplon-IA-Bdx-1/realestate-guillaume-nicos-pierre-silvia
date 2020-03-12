FROM python:3.7-buster

COPY ./requirements.txt /app/requirements.txt
COPY ./www /app/www
COPY ../models /app/www


WORKDIR /app
RUN pip install -r requirements.txt

WORKDIR /app/www
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
