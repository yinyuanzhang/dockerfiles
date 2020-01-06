FROM php:5.6-cli

RUN apt-get update -y \
     && apt-get install -y curl git unzip
RUN cd ~ \
     && curl -sS https://getcomposer.org/installer -o composer-setup.php \
     && php composer-setup.php --install-dir=/usr/local/bin --filename=composer

ENV NVM_DIR /usr/local/nvm

RUN mkdir -p $NVM_DIR

ENV NODE_VERSION 10.15.3

# install nvm
# https://github.com/creationix/nvm#install-script
RUN curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash

# install node and npm
RUN . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

# add node and npm to path so the commands are available
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

RUN composer global require --no-plugins --no-scripts phpro/grumphp
ENV PATH /root/.composer/vendor/bin/:$PATH

CMD ["grumphp"]
