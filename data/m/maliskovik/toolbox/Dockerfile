################################################################################
#                                                                              #
#                                 {o,o}                                        #
#                                 |)__)                                        #
#                                 -"-"-                                        #
#                                                                              #
################################################################################
#
#
#
#################################---FROM---#####################################

FROM php

################################################################################

#################################---INFO---#####################################

MAINTAINER Lovrenc Avsenek <a.lovrenc@gmail.com>

################################################################################

#################################---ENV---######################################

ENV export DEBIAN_FRONTEND noninteractive

################################################################################

################################---BUILD---#####################################

RUN apt update; \
    apt install -q -y \
      git \
      curl \
      wget \
      build-essential \
      make \
      unzip \
      npm; \
    ln -s /usr/bin/nodejs /usr/bin/node; \
    curl -sL https://deb.nodesource.com/setup_6.x | bash -; \
    apt install -y -q nodejs; \
    npm install -g npm; \
    npm install -g \
      bower \
      grunt \
      grunt-cli \
      gulp \
      load-grunt-tasks \
      time-grunt; \
    curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer; \
    apt-get autoremove -y; \
    apt-get clean

################################################################################
