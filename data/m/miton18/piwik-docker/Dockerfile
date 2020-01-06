FROM tutum/apache-php:latest

ENV ALLOW_OVERRIDE=true

RUN apt-get update
RUN apt-get install -yq git
RUN apt-get install -yq gzip
RUN apt-get install -yq wget

RUN /usr/local/bin/composer self-update

RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /app

# Lunch a specific version
#RUN git clone -v --branch 2.16.1 https://github.com/piwik/piwik /app
RUN git clone -v https://github.com/piwik/piwik /app

RUN composer install

RUN wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz

RUN gunzip GeoLiteCity.dat.gz

RUN cp GeoLiteCity.dat /app/misc

EXPOSE 443
