FROM ubuntu:trusty

MAINTAINER robmiller

RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-dev sqlite3 supervisor python-setuptools git ssh-client python3-psycopg2
#RUN add-apt-repository -y ppa:nginx/stable
#RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install -y libjpeg-dev zlib1g-dev

RUN mkdir -p /code/app
RUN mkdir -p /code/logs
RUN mkdir -p /code/backups


ADD ./* /code/
ADD ./run.sh /usr/local/bin/

RUN pip3 install -r /code/requirements.txt
RUN pip3 install uwsgi

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default

RUN ln -s /code/nginx-app.conf /etc/nginx/sites-enabled/
RUN ln -s /code/supervisor-app.conf /etc/supervisor/conf.d/

RUN mkdir /etc/nginx/ssl
ADD ./nginx.crt /etc/nginx/ssl/
ADD ./nginx.key /etc/nginx/ssl/

RUN django-admin startproject website /code/app
RUN cd /code/app && python3 ./manage.py makemigrations --noinput && python3 ./manage.py migrate --noinput

#Run cron
RUN crontab /code/crontab
#ADD crontab-sendemails /etc/cron.d/sendemails
#RUN chmod 0644 /etc/cron.d/sendemails
#RUN touch /var/log/cron.log


# This line doesn't work. Instead collect the static when the app has been added. 	
#RUN cd /code/app && python3 ./manage.py collectstatic --noinput

EXPOSE 80
CMD ["/bin/bash", "/usr/local/bin/run.sh"]


