# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
ARG BASE_CONTAINER=jupyter/all-spark-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Abby Chau <i@abby.md>"

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    php7.2 \
    php-pear php7.2-curl php7.2-dev php7.2-gd \
    php7.2-mbstring php7.2-zip php7.2-mysql \
    php7.2-xml pkg-config libzmq3-dev\
    gcc && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://raw.githubusercontent.com/composer/getcomposer.org/1b137f8bf6db3e79a38a5bc45324414a6b1f9df2/web/installer -O - -q | php -- --quiet
RUN pecl config-set php_ini /etc/php/7.2/cli/php.ini
RUN pear config-set php_ini /etc/php/7.2/cli/php.ini
RUN echo '' | pecl install zmq-beta
RUN wget https://litipk.github.io/Jupyter-PHP-Installer/dist/jupyter-php-installer.phar

USER $NB_UID
RUN php ./jupyter-php-installer.phar install -vvv
RUN rm *.phar
RUN pip install tensorflow
ADD notebook-sample $HOME/notebook-sample 