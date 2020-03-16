FROM python:3.7-buster

RUN apt-get update && apt-get -y install cron dos2unix

COPY ./training_container/requirements.txt /app/python/requirements.txt
COPY ./training_container/Model.py /app/python/training.py
COPY ./scrapper/query.py /app/python/query.py
COPY ./scrapper/annonce.py /app/python/annonce.py
COPY ./training_container/.env /app/python/.env
COPY ./training_container/init.sh /app/init.sh
RUN chmod 0700 /app/init.sh

RUN dos2unix /app/init.sh

WORKDIR /app/python

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN /usr/local/bin/python -m pip install -r requirements.txt

COPY ./training_container/training.cron /etc/crond.d/training.cron
RUN dos2unix /etc/crond.d/training.cron
RUN chmod 0644 /etc/crond.d/training.cron
RUN crontab -u root /etc/crond.d/training.cron
RUN touch /var/log/cron.log

CMD ["/bin/sh", "/app/init.sh"]
