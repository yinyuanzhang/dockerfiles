FROM kouinkouin/php-cli:7.1

RUN apt-get update \
  && apt-get install -y mysql-client \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ADD files/tools /srv/tools

RUN chmod +x /srv/tools/ps-*

