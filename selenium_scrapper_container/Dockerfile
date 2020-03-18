FROM python:3.7-buster

RUN apt-get update && apt-get -y install cron dos2unix bsdtar

RUN curl http://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip | bsdtar -xvf - -C /usr/local/bin/
RUN chmod 0755 /usr/local/bin/chromedriver

COPY ./selenium_scrapper_container/requirements.txt /app/python/requirements.txt
COPY ./scrapper/query.py /app/python/query.py
COPY ./scrapper/annonce.py /app/python/annonce.py
COPY ./training_container/.env /app/python/.env
COPY ./selenium_scrapper_container/init.sh /app/init.sh
RUN chmod 0700 /app/init.sh

RUN dos2unix /app/init.sh


WORKDIR /app/python

RUN wget https://dl.google.com/linux/direct/google-chrome-beta_current_amd64.deb
RUN ls
RUN apt-get install --fix-broken /app/python/google-chrome-beta_current_amd64.deb -y
RUN rm /app/python/google-chrome-beta_current_amd64.deb

RUN apt-get install nano

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN /usr/local/bin/python -m pip install -r requirements.txt

CMD tail -f /dev/null

# COPY ./selenium_scrapper_container/scrapping.cron /etc/crond.d/scrapping.cron
# RUN dos2unix /etc/crond.d/scrapping.cron
# RUN chmod 0644 /etc/crond.d/scrapping.cron
# RUN crontab -u root /etc/crond.d/scrapping.cron
# RUN touch /var/log/cron.log

# CMD ["/bin/sh", "/app/init.sh"]
# CMD ["/bin/sh", "-c", "sleep 1000"]