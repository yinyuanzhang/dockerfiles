FROM joaolboing/ubuntu:14.04

RUN apt-get update && \
apt-get install -y apache2 supervisor libxrender1 libxext6 && \
a2enmod rewrite && \
a2enmod proxy && \
a2enmod proxy_http

RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/supervisor

ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf


ADD start-apache2.sh /start-apache2.sh
ADD run.sh /run.sh
RUN chmod 755 /*.sh

EXPOSE 80
CMD ["/run.sh"]
