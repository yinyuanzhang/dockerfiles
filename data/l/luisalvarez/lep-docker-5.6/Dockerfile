FROM ubuntu:trusty
# maintainer by luis inspire in solucionesgbh/lep image
MAINTAINER Luis Alvarez <l.alvarez@gbh.com.do> 


# Install Dependecies
RUN apt-get update && \
  apt-get install -y --force-yes software-properties-common curl && \
  apt-add-repository ppa:ondrej/php -y && \
  apt-get update && \
  apt-get install -y --force-yes php5.6-fpm php5.6-cli php5.6-dev \
    php5.6-pgsql php5.6-sqlite3 php5.6-gd  php5.6-common \
    php5.6-curl  php-pear php5.6-memcached \
    php5.6-imap php5.6-imagick php5.6-mysql php5.6-mbstring \
    php5.6-xml php5.6-zip php5.6-bcmath php5.6-soap \
    php5.6-intl php5.6-readline \
    nginx \
    curl \
    zip \ 
    supervisor \
    git \
    php5.6-mcrypt

# Enable mcrypt
RUN phpenmod mcrypt

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer


# Install node, bower and gulp-cli
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.6/install.sh | bash
ENV NODE_VER v6.11.1
ENV NVM_DIR "/root/.nvm"
RUN [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" \
    && nvm install $NODE_VER \
    && nvm alias default $NODE_VER \
    && nvm use default \
    && npm install -g bower gulp-cli
ENV BASE_NODE_PATH $NVM_DIR/versions/node
ENV NODE_PATH $BASE_NODE_PATH/$NODE_VER/lib/node_modules
ENV PATH $BASE_NODE_PATH/$NODE_VER/bin:$PATH


# Confs
RUN mkdir /run/php
COPY nginx/default /etc/nginx/sites-available
COPY supervisord /etc/supervisor/conf.d
RUN sed -i "s/error_reporting = .*/error_reporting = E_ALL/" /etc/php/5.6/cli/php.ini && \
    sed -i "s/display_errors = .*/display_errors = On/" /etc/php/5.6/cli/php.ini && \
    sed -i "s/memory_limit = .*/memory_limit = 512M/" /etc/php/5.6/cli/php.ini && \
    sed -i "s/;date.timezone.*/date.timezone = UTC/" /etc/php/5.6/cli/php.ini && \
    sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/5.6/fpm/php.ini && \
    sed -i "s/memory_limit = .*/memory_limit = 512M/" /etc/php/5.6/fpm/php.ini && \
    sed -i "s/upload_max_filesize = .*/upload_max_filesize = 100M/" /etc/php/5.6/fpm/php.ini && \
    sed -i "s/post_max_size = .*/post_max_size = 100M/" /etc/php/5.6/fpm/php.ini && \
    sed -i "s/;date.timezone.*/date.timezone = UTC/" /etc/php/5.6/fpm/php.ini && \
    sed -i "s/error_reporting = .*/error_reporting = E_ALL/" /etc/php/5.6/fpm/php.ini && \
    sed -i "s/max_execution_time = .*/max_execution_time = 300/" /etc/php/5.6/fpm/php.ini && \
    sed -i "s/display_errors = .*/display_errors = On/" /etc/php/5.6/fpm/php.ini

# Add our init script
ADD run.sh /run.sh
RUN chmod 755 /run.sh

RUN mkdir /app
WORKDIR /app
RUN mkdir /app/public && touch /app/public/index.php && echo '<?php phpinfo();?>' > /app/public/index.php

EXPOSE 80

CMD ["/run.sh"]
