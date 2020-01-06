FROM laradock/php-fpm:2.5-7.1
RUN php -v
RUN apt-get update
RUN apt-get -y install apt-utils
RUN apt-get -y install sshpass
RUN apt-get -y -qq install npm
RUN apt-get -y -qq install build-essential libssl-dev

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 7.6.0

# Install nvm with node and npm
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash \
    && export NVM_DIR="/usr/local/nvm" \
    && [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/v$NODE_VERSION/bin:$PATH

RUN npm install --global gulp
RUN curl -sS https://getcomposer.org/installer -o composer-setup.php
RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer
