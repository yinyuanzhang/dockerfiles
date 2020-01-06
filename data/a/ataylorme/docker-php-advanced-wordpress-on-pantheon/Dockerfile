# Start with PHP 7.2
FROM devwithlando/php:7.2-fpm

# Update
RUN apt-get update 

# Install wget
RUN \
	echo -e "\nInstalling wget..." && \
	apt-get install -y wget

# Install openssl
RUN \
	echo -e "\nInstalling openssl..." && \
	apt-get install -y openssl

# Install rsync
RUN \
	echo -e "\nInstalling rsync..." && \
	apt-get install -y rsync

# Install jq
RUN \
	echo -e "\nInstalling jq..." && \
	apt-get install -y jq

# Install ssh
RUN \
	echo -e "\nInstalling ssh..." && \
	apt-get install -y openssh-client

# Install Terminus
RUN \
	echo -e "\nInstalling Terminus 2.x..." && \
	/usr/bin/env COMPOSER_BIN_DIR=$HOME/bin composer --working-dir=$HOME require pantheon-systems/terminus "^2"

# Enable Composer parallel downloads
RUN \
	echo -e "\nInstalling hirak/prestissimo for parallel Composer downloads..." && \
	composer global require -n "hirak/prestissimo:^0.3"

# Install Terminus plugins
RUN \
	echo -e "\nInstalling Terminus plugins..." && \
	mkdir -p $HOME/.terminus/plugins && \
	composer create-project -n -d $HOME/.terminus/plugins pantheon-systems/terminus-build-tools-plugin:dev-master && \
	composer create-project -n -d $HOME/.terminus/plugins pantheon-systems/terminus-secrets-plugin:^1

RUN \
	echo -e "\nInstalling headless Chrome..."

ENV DISPLAY=:99 \
    DBUS_SESSION_BUS_ADDRESS=/dev/null

RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /usr/local/etc/php-fpm.conf \
 && sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" /usr/local/etc/php-fpm.d/www.conf \
 && sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g" /usr/local/etc/php-fpm.d/www.conf \
 && sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g" /usr/local/etc/php-fpm.d/www.conf \
 && sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g" /usr/local/etc/php-fpm.d/www.conf \
 && sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g" /usr/local/etc/php-fpm.d/www.conf \
 && sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g" /usr/local/etc/php-fpm.d/www.conf

RUN apt-get update -qqy \
  && apt-get -qqy install wget ca-certificates apt-transport-https nginx supervisor ttf-wqy-zenhei fonts-unfonts-core \
    unzip git x11vnc xfonts-100dpi xfonts-75dpi xfonts-cyrillic xfonts-scalable xvfb libpng-dev libjpeg-dev gnupg \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install google-chrome-stable google-chrome-unstable chromium google-chrome-beta \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN docker-php-ext-install gd

RUN useradd headless --shell /bin/bash --create-home \
  && usermod -a -G sudo headless \
  && echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \
  && echo 'headless:nopassword' | chpasswd

RUN mkdir /data

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
 && rm -rf /etc/nginx/sites-enabled/default \
 && mkdir -p /root/.ssh \
 && echo "Host *\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config

VOLUME /code

WORKDIR /code

COPY files/supervisord.conf /etc/supervisord.conf

COPY files/entrypoint.sh /entrypoint.sh

COPY files/vhost.conf /etc/nginx/sites-enabled/vhost.conf

ENTRYPOINT ["/entrypoint.sh"]

CMD ["bash"]
