FROM codingwell/rpi-raspbian-qemu

COPY assets/bin /usr/local/bin/
RUN [ "cross-build-start" ]

RUN \
 echo "deb http://mirrordirector.raspbian.org/raspbian/ stretch main" >> /etc/apt/sources.list.d/mirrordirector.list && \
 apt-key adv --fetch-keys http://mirrordirector.raspbian.org/raspbian.public.key && \
 echo "APT::Default-Release "jessie";" > /etc/apt/apt.conf.d/default-release \
 && apt-get update \
 && apt-get install -y \
 curl \
 && apt-get install -y -t stretch \
 php7.0-curl \
 php7.0-fpm \ 
 php7.0-gd \ 
 php7.0-intl \
 php7.0-mbstring \
 php7.0-mcrypt \
 php7.0-mysql \ 
 php7.0-opcache \
 php7.0-zip \
 php-apcu \ 
 php-geoip \
 php-xml \ 
 && \
  set -ex \
    && cd /etc/php/7.0/fpm \
    && { \
        echo '[global]'; \
        echo 'error_log = /proc/self/fd/2'; \
        echo; \
        echo '[www]'; \
        echo '; if we send this to /proc/self/fd/1, it never appears'; \
        echo 'access.log = /proc/self/fd/2'; \
        echo; \
        echo 'clear_env = no'; \
        echo; \
        echo '; Ensure worker stdout and stderr are sent to the main error log.'; \
        echo 'catch_workers_output = yes'; \
    } | tee pool.d/docker.conf \
    && { \
        echo '[global]'; \
        echo 'daemonize = no'; \
        echo; \
        echo '[www]'; \
        echo 'listen = [::]:9000'; \
    } | tee pool.d/zz-docker.conf \
    && \
    \
#Install piwik
    curl -fsSL -o piwik.tar.gz \
      "https://builds.piwik.org/piwik-latest.tar.gz" \
    && curl -fsSL -o piwik.tar.gz.asc \
          "https://builds.piwik.org/piwik-latest.tar.gz.asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 814E346FA01A20DBB04B6807B5DBD5925590A237 \
    && gpg --batch --verify piwik.tar.gz.asc piwik.tar.gz \
    && rm -r "$GNUPGHOME" piwik.tar.gz.asc \
    && tar -xzf piwik.tar.gz -C /usr/src \
    && rm piwik.tar.gz \
    && \
    curl -fsSL -o /usr/src/piwik/misc/GeoIPCity.dat.gz http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz \
    && gunzip /usr/src/piwik/misc/GeoIPCity.dat.gz \
    && tar czf /usr/src/piwik.tar.gz -C /usr/src/piwik . \
    && rm -r /usr/src/piwik \
    &&  { \
      echo 'always_populate_raw_post_data=-1'; \
      echo 'sendmail_path = /usr/sbin/ssmtp -t'; \
      echo 'geoip.custom_directory=/var/www/html/piwik/misc'; \
      } | tee /etc/php/7.0/fpm/php.ini \ 
    && mkdir /var/run/php \
    # Cleanup
    apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN [ "cross-build-end" ]

VOLUME /var/www/html
WORKDIR /var/www/html
EXPOSE 9000

ENTRYPOINT ["entrypoint.sh"]
CMD ["php-fpm7.0"]