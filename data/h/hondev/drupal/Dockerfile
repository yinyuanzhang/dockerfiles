
FROM devwithlando/php:7.2-apache-2

RUN apt-get update -y \
  && apt-get upgrade -y \
  && apt-get install -y default-jdk \
  && wget -O /tmp/google-chrome-stable_current_amd64.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && apt install /tmp/google-chrome-stable_current_amd64.deb -y \
  && curl -sL https://deb.nodesource.com/setup_10.x | bash && apt-get install -y nodejs \
  && npm install -g n \
  && n 10 \
  && rm -rf \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /var/lib/cache/* \
  && rm -rf /var/lib/log/* \
  && rm -rf /tmp/* \
  && touch /root/.bashrc

COPY ./etc/apache2/conf-available/docker-php.conf /etc/apache2/conf-available/docker-php.conf
COPY ./etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY ./etc/apache2/apache2.conf /etc/apache2/apache2.conf
COPY ./usr/local/etc/php/php.ini /usr/local/etc/php/php.ini
COPY ./root/.gitconfig /root/.gitconfig
