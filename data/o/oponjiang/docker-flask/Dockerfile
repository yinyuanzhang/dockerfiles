FROM ubuntu:14.04

MAINTAINER CM

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get -y install nginx  sed python-pip python-dev uwsgi-plugin-python supervisor
#libmysqlclient-dev

RUN mkdir -p /var/log/nginx/app
RUN mkdir -p /var/log/uwsgi/app/


RUN rm /etc/nginx/sites-enabled/default
COPY flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN mkdir -p /etc/uwsgi
COPY uwsgi.ini /etc/uwsgi/uwsgi.ini

RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
# Facebook login
RUN pip install http://github.com/pythonforfacebook/facebook-sdk/tarball/master

CMD ["/usr/bin/supervisord"]
