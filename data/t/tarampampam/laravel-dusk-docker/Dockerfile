FROM composer:1.8.0 AS composer

FROM debian:jessie

MAINTAINER "Tarampampam <tarampampam@users.noreply.github.com>"
LABEL Description="Image for running laravel/dusk test (php 7.1 included)" Vendor="Tarampampam" Version="0.1"

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN \
  apt-get -yq update && apt-get -yq upgrade -o Dpkg::Options::="--force-confold" \
  && apt-get -yq install --no-install-recommends apt-utils lsb-release apt-transport-https curl zip unzip bzip2 \
    git ca-certificates net-tools

RUN \
  curl -o /etc/apt/trusted.gpg.d/php.gpg  https://packages.sury.org/php/apt.gpg \
  && echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list \
  && apt-get -yq update && apt-get install -y php7.1-common php7.1-cli php7.1-xml php7.1-zip php7.1-curl php7.1-bcmath \
    php7.1-json php7.1-mbstring php7.1-pgsql php7.1-mcrypt php7.1-redis php7.1-sqlite3 php7.1-mysql php7.1-gd \
    php7.1-imagick imagemagick \
  && update-alternatives --set php $(which php7.1)

ENV COMPOSER_ALLOW_SUPERUSER="1" \
    COMPOSER_HOME="/tmp/composer" \
    PATH="$COMPOSER_HOME/vendor/bin:$PATH"

COPY --from=composer /usr/bin/composer /usr/bin/composer

RUN composer --no-interaction global require 'hirak/prestissimo'

ADD xvfb.init.sh /etc/init.d/xvfb
RUN \
  apt-get install -yq xvfb gconf2 fonts-ipafont-gothic xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base \
    xfonts-scalable \
  && chmod +x /etc/init.d/xvfb \
  && CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` \
  && mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION \
  && curl -sS -o /tmp/chromedriver_linux64.zip \
    http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip \
  && unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION \
  && rm /tmp/chromedriver_linux64.zip \
  && chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver \
  && ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver \
  && curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get -yqq update && apt-get -yqq install google-chrome-stable x11vnc

RUN apt-get install -y supervisor
ADD supervisord.conf /etc/supervisor/supervisord.conf

# Copy entypoint script
COPY ./docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod -v +x /*.sh && apt-get -yqq clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 9515

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
