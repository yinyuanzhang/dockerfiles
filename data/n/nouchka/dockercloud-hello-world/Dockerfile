FROM nouchka/symfony:7.0

COPY www/ /var/www/html/

RUN rm -rf /var/www/html/index.html

RUN echo "export HOSTNAME=`hostname`" >> /etc/apache2/envvars
