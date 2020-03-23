FROM python:3.7-buster

COPY ./prediction_container/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY ./prediction_container/www /app/www

WORKDIR /app/www
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
