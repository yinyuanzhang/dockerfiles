FROM i386/ubuntu:18.04


ENV DEBIAN_FRONTEND=noninteractive

ENV TZ=Australia/Sydney
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update \
    && apt-get install -y git net-tools vim nginx rsyslog supervisor php7.2-fpm php7.2-cli apache2-utils\
    && rm -rf /var/lib/apt/lists/* \

RUN rm -rf /var/www && git clone https://github.com/potsky/PimpMyLog.git /var/www
RUN sed -i -e 's/;daemonize\ =\ yes/daemonize\ =\ no/' /etc/php/7.2/fpm/php-fpm.conf

RUN sed -i 's/variables_order\ =\ "GPCS"/variables_order\ =\ \"GPCSE\"'/ /etc/php/7.2/cli/php.ini
RUN sed -i 's/;date.timezone\ =/date.timezone\ =\ Australia\/Sydney/' /etc/php/7.2/cli/php.ini             
RUN sed -i -e 's/#module(load="imudp")/module(load="imudp")/' -e 's/#input(type="imudp"\ port="514")/input(type="imudp"\ port="514")/' /etc/rsyslog.conf

RUN mkdir -p /var/log/net/ && touch /var/log/net/syslog.log && ln -s /var/log/net/syslog.log /var/www/
RUN chown -R syslog:adm /var/log/net/
RUN adduser www-data adm

COPY nginx.conf /etc/nginx/nginx.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY config.user.php /var/www/config.user.php
COPY rsyslog.conf /etc/rsyslog.conf
COPY create-user.php /var/www/
RUN htpasswd -c -b /etc/nginx/.htpasswd sysadmin syspassword
RUN cd /var/www && php7.2 -f create-user.php && chown www-data:www-data config.auth.user.php && rm -f create-user.php 
#EXPOSE 80 514/udp

CMD ["service","php7.2-fpm","start","&&","service","supervisor","start"]
