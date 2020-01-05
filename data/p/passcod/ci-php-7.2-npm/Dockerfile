FROM circleci/php:7.2-node

RUN sudo apt install -y build-essential ccache file re2c \
      libicu-dev libldap2-dev libxml2-dev libgmp-dev libmhash-dev libmcrypt-dev \
  && sudo ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/local/include/ \
  && sudo docker-php-ext-configure gmp \
  && sudo docker-php-ext-install gmp \
  && sudo docker-php-ext-install bcmath \
  && sudo docker-php-ext-install intl \
  && sudo docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
  && sudo docker-php-ext-install ldap \
  && echo "short_open_tag = On" | sudo tee /usr/local/etc/php/conf.d/short_tags.ini

RUN sudo npm i -g npm \
  && sudo composer self-update

ENV PATH="/usr/lib/ccache:${PATH}"
