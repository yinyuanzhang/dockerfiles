FROM drupal:7.56

RUN apt-get update -y \
 && apt-get install -y \
      libxml2-dev \
      wget \
      python-dev \
      python-pip \
      drush \
 && apt-get clean -y \
 && docker-php-ext-install soap \
 && cd /root/ \
 && wget https://github.com/edenhill/librdkafka/archive/v0.11.0.tar.gz \
 && tar -xzf v0.11.0.tar.gz \
 && cd /root/librdkafka-0.11.0 \
 && ./configure \
 && make \
 && make install \
 && pecl install rdkafka \
 && echo "extension=rdkafka.so" > /usr/local/etc/php/conf.d/rdkafka.ini \
 && pip install --upgrade supervisor supervisor-stdout

COPY supervisord.conf /etc/

ENTRYPOINT ["supervisord"]

CMD ["-c", "/etc/supervisord.conf"]