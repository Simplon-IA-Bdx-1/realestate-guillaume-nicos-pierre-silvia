FROM python:3.7-buster

RUN apt-get update && apt-get -y install cron

COPY ./training_container/requirements.txt /app/python/requirements.txt
COPY ./training_container/Model.py /app/python/training.py
COPY ./scrapper/query.py /app/python/query.py
COPY ./scrapper/annonce.py /app/python/annonce.py

WORKDIR /app/python

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./training_container/training.cron /etc/crond.d/training.cron
RUN chmod 0644 /etc/crond.d/training.cron
RUN crontab -u root /etc/crond.d/training.cron
RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log





#WORKDIR /app/www
#ENTRYPOINT [ "python" ]
#CMD [ "app.py" ]
