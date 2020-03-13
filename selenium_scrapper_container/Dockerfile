FROM python:3.7-buster

RUN apt-get update && apt-get -y install cron dos2unix bsdtar

RUN curl http://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip | bsdtar -xvf - -C /usr/local/bin/

COPY ./training_container/requirements.txt /app/python/requirements.txt
COPY ./scrapper/query.py /app/python/query.py
COPY ./scrapper/annonce.py /app/python/annonce.py
COPY ./training_container/.env /app/python/.env
COPY ./selenium_scrapper_container/init.sh /app/init.sh
RUN chmod 0700 /app/init.sh

RUN dos2unix /app/init.sh


WORKDIR /app/python

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN /usr/local/bin/python -m pip install -r requirements.txt

COPY ./selenium_scrapper_container/scrapping.cron /etc/crond.d/scrapping.cron
RUN dos2unix /etc/crond.d/scrapping.cron
RUN chmod 0644 /etc/crond.d/scrapping.cron
RUN crontab -u root /etc/crond.d/scrapping.cron
RUN touch /var/log/cron.log

#CMD cron && tail -f /var/log/cron.log
CMD ["/bin/sh", "/app/init.sh"]

CMD ["/bin/sh", "-c", "sleep 1000"]


#WORKDIR /app/www
#ENTRYPOINT [ "python" ]
#CMD [ "app.py" ]
