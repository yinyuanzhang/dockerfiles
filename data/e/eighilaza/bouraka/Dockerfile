FROM python:3.4

RUN mkdir -p /bouraka
WORKDIR /bouraka

COPY requirements.txt /bouraka/
RUN pip install -U pip
RUN pip install -r /bouraka/requirements.txt

RUN apt-get -y update && apt-get install -y apache2 libapache2-mod-wsgi-py3 supervisor

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
COPY apache/000-default.conf /etc/apache2/sites-available/

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#FOR EASIER DEBUG
RUN apt-get -y install vim

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
