FROM ubuntu:14.04

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/run/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2

COPY packages /packages
RUN dpkg -i packages/*

RUN mkdir /var/run/apache2

ADD index.html /var/www/html/
ADD cgi-bin /usr/lib/cgi-bin/
RUN chmod +x /usr/lib/cgi-bin/test-app.cgi

RUN a2enmod cgid

# Install vulnerable bash
COPY bash-4.3 /bash-4.3
WORKDIR /bash-4.3
RUN ./configure && \
    make && \
    make install
WORKDIR /
RUN rm -rf /bash-4.3 && rm -rf packages/

EXPOSE 80

CMD ["/usr/sbin/apache2", "-DFOREGROUND"]
