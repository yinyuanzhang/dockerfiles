FROM ubuntu:16.04

RUN echo "deb http://archive.ubuntu.com/ubuntu/ xenial main universe" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y vim net-tools nginx supervisor python-pip python-dev build-essential \
                   && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
                   && rm /etc/nginx/sites-enabled/* && rm /etc/nginx/sites-available/* \
                   && pip install gearman PyYAML

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY reloader.py /reloader.py

COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["/usr/bin/supervisord"]
