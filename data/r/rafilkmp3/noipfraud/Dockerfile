FROM dockerqa/unzip

ADD http://noipfraud.com/download/latest /tmp/noipfraud.zip

#ADD noipfraud.zip /tmp/sendy.zip
RUN unzip /tmp/noipfraud.zip -d /tmp/www/
RUN ls /tmp/www

FROM php:7.2-apache
#COPY src/ /var/www/html/
ENV DOCUMENTROOT /var/www/html 
ENV DEBIAN_FRONTEND=noninteractive

COPY --from=0 /tmp/www/ ${DOCUMENTROOT}/activate

RUN apt-get update && apt-get -y upgrade && apt-get -y install \
    libmcrypt-dev curl vim && \ 
    pecl install mcrypt-1.0.2 apcu && \ 
    docker-php-ext-enable mcrypt apcu && \ 
    rm -rf /var/lib/apt/lists/*

RUN chmod 777 -R ${DOCUMENTROOT}
COPY run.sh /run.sh
RUN chmod +x /run.sh
EXPOSE 80

CMD ["/run.sh"]
