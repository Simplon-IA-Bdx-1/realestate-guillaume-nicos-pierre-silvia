FROM python:3.7-buster
WORKDIR /app/python
RUN apt-get update && apt-get -y install cron dos2unix bsdtar nano

RUN curl http://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_linux64.zip | bsdtar -xvf - -C /usr/local/bin/
RUN chmod 0755 /usr/local/bin/chromedriver

RUN perl -pi -e 's/cdc_/abc_/g' /usr/local/bin/chromedriver

RUN wget https://dl.google.com/linux/direct/google-chrome-beta_current_amd64.deb
RUN ls
RUN apt-get install --fix-broken /app/python/google-chrome-beta_current_amd64.deb -y
RUN rm /app/python/google-chrome-beta_current_amd64.deb

RUN /usr/local/bin/python -m pip install --upgrade pip
COPY ./selenium_scrapper_container/requirements.txt /app/python/requirements.txt
RUN /usr/local/bin/python -m pip install -r requirements.txt


COPY ./scrapper/query.py /app/python/query.py
COPY ./scrapper/annonce.py /app/python/annonce.py
COPY ./scrapper/selenium_scrapper.py /app/python/selenium_scrapper.py
COPY ./scrapper/scrap.py /app/python/scrap.py
COPY ./training_container/.env /app/python/.env
COPY ./selenium_scrapper_container/init.sh /app/init.sh
RUN chmod 0700 /app/init.sh

RUN dos2unix /app/init.sh
# CMD tail -f /dev/null

COPY ./selenium_scrapper_container/selenium.cron /etc/crond.d/selenium.cron
# RUN dos2unix /etc/crond.d/selenium.cron
RUN mkdir -p /app/python/pages
CMD echo Starting && /usr/local/bin/python /app/python/selenium_scrapper.py
# RUN dos2unix /etc/crond.d/scrapping.cron
# RUN chmod 0644 /etc/crond.d/scrapping.cron
# RUN crontab -u root /etc/crond.d/scrapping.cron
# RUN touch /var/log/cron.log

# CMD ["/bin/sh", "/app/init.sh"]
# CMD ["/bin/sh", "-c", "sleep 1000"]
