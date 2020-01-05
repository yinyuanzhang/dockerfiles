FROM alpine
MAINTAINER Jimmy Koo <kukkiz@gmail.com>
ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.docker.dockerfile="/Dockerfile" \
      org.label-schema.license="GPL v3" \
      org.label-schema.name="Docker-Ampache" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-type="Git" \
      org.label-schema.vcs-url="https://bitbucket.org/jkoo/docker-ampache-app/src"

ENV aVersion 3.8.2

RUN apk add --update apache2 apache2-utils php5
RUN apk add php5-xml php5-json php5-pdo php5-pdo_mysql php5-curl php5-iconv php5-apache2 php5-openssl php5-zlib php5-gd
RUN apk add openrc unzip inotify-tools wget
RUN apk add php5-gettext

WORKDIR /

# Swith these two lines for local debug
ADD https://github.com/ampache/ampache/releases/download/${aVersion}/ampache-${aVersion}_all.zip /ampache_all.zip
#COPY ampache_all.zip /ampache_all.zip

ADD start.sh /start.sh
ADD 001-ampache.conf /etc/apache2/conf.d/001-ampache.conf

#RUN rm -rf /var/www/* && \
RUN unzip -q /ampache_all.zip -d /var/www/localhost/htdocs/ampache && \
    chown -R apache:www-data /var/www && \
    chmod 755 /*.sh && \
    sed -i 's/#\(.*rewrite_module.*\)/\1/g' /etc/apache2/httpd.conf && \
    echo 'PidFile /var/www/apache2.pid' >> /etc/apache2/httpd.conf && \
    echo '30 7 * * * apache www-data /var/www/localhost/ampache/bin/catalog_update.inc' >> /etc/crontab

VOLUME ["/media", "/var/www/config", "/var/www/themes"]

EXPOSE 80

CMD ["/start.sh"]
