FROM ubuntu:latest


MAINTAINER simon

#### global common #############################
ARG ARG_RUN_ENV=production
ENV RUN_ENV=${ARG_RUN_ENV}
ARG ARG_CONTAINER_CODE_PATH=/var/www
ENV CONTAINER_CODE_PATH=${ARG_CONTAINER_CODE_PATH}
ARG ARG_WORKSPACE_CONFIG=/config
ENV WORKSPACE_CONFIG=${ARG_WORKSPACE_CONFIG}
ARG ARG_WORKSPACE_DATA=/data


#### silent installation #############################
ARG DEBIAN_FRONTEND=noninteractive


#### user and group #############################
ARG ARG_APP_RUN_PUID=1000
ARG ARG_APP_RUN_PGID=1000
ARG ARG_APP_RUN_NAME=crcms
ARG ARG_APP_RUN_GROUP=crcms
ENV APP_RUN_PUID=${ARG_APP_RUN_PUID}
ENV APP_RUN_PGID=${ARG_APP_RUN_PGID}
ENV APP_RUN_NAME=${ARG_APP_RUN_NAME}
ENV APP_RUN_GROUP=${ARG_APP_RUN_GROUP}
RUN groupadd -g ${ARG_APP_RUN_PGID} ${ARG_APP_RUN_GROUP} && \
    useradd -u ${ARG_APP_RUN_PUID} -g ${ARG_APP_RUN_PGID} ${ARG_APP_RUN_NAME} && \
    usermod -s /sbin/nologin ${ARG_APP_RUN_NAME}


#### software base #############################
RUN apt-get update -yqq \
    && apt-get install -y rsyslog \
    && apt-get install -y curl \
    && apt-get install -y apt-utils \
    # php
    && apt-get install -y php7.2-dev \
    && apt-get install -y php7.2-pdo-mysql \
    && apt-get install -y php7.2-mbstring \
    && apt-get install -y php7.2-curl \
    && apt-get install -y php7.2-zip \
    && apt-get install -y php7.2-gd \
    && apt-get install -y php7.2-bcmath \
    && apt-get install -y composer


#### npm #############################
ARG ARG_WORKSPACE_INSTALL_NPM=false
RUN if [ ${ARG_WORKSPACE_INSTALL_NPM} = true ]; then \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install -y nodejs \
    && apt-get install -y build-essential \
;fi


#### crontab #############################
ARG ARG_WORKSPACE_INSTALL_CRONTAB=true
RUN if [ ${ARG_WORKSPACE_INSTALL_CRONTAB} = true ]; then \
    apt-get install -y cron \
;fi


#### supervisor #############################
ARG ARG_WORKSPACE_INSTALL_SUPERVISOR=true
RUN if [ ${ARG_WORKSPACE_INSTALL_SUPERVISOR} = true ]; then \
    apt-get install -y supervisor \
;fi


#### set timezone #############################
ARG ARG_TIMEZONE=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/${ARG_TIMEZONE} /etc/localtime && echo ${ARG_TIMEZONE} > /etc/timezone


#### php pecl #############################
ARG ARG_PHP_MODS_AVAILABLE_PATH=/etc/php/7.2/mods-available
ARG ARG_PHP_CONF_PATH=/etc/php/7.2/cli/conf.d
# swoole
ARG ARG_WORKSPACE_INSTALL_SWOOLE=true
RUN if [ ${ARG_WORKSPACE_INSTALL_SWOOLE} = true ]; then \
    pecl install swoole \
    && echo "extension=swoole.so" > ${ARG_PHP_MODS_AVAILABLE_PATH}/swoole.ini \
    && ln -s ${ARG_PHP_MODS_AVAILABLE_PATH}/swoole.ini ${ARG_PHP_CONF_PATH}/20-swoole.ini \
;fi

# mongodb
ARG ARG_WORKSPACE_INSTALL_MONGODB=true
RUN if [ ${ARG_WORKSPACE_INSTALL_MONGODB} = true ]; then \
    pecl install mongodb \
    && echo "extension=mongodb.so" > ${ARG_PHP_MODS_AVAILABLE_PATH}/mongodb.ini \
    && ln -s ${ARG_PHP_MODS_AVAILABLE_PATH}/mongodb.ini ${ARG_PHP_CONF_PATH}/20-mongodb.ini \
;fi

# redis
ARG ARG_WORKSPACE_INSTALL_REDIS=true
RUN if [ ${ARG_WORKSPACE_INSTALL_REDIS} = true ]; then \
    #reids needs igbinary
    pecl install igbinary \
    && echo "extension=igbinary.so" > ${ARG_PHP_MODS_AVAILABLE_PATH}/igbinary.ini \
    && ln -s ${ARG_PHP_MODS_AVAILABLE_PATH}/igbinary.ini ${ARG_PHP_CONF_PATH}/20-igbinary.ini \
    && pecl install redis \
    && echo "extension=redis.so" > ${ARG_PHP_MODS_AVAILABLE_PATH}/redis.ini \
    && ln -s ${ARG_PHP_MODS_AVAILABLE_PATH}/redis.ini ${ARG_PHP_CONF_PATH}/20-redis.ini \
;fi


#### clear #############################
# clear Ubuntu image will run automatically apt-get clean,so is not need apt-get clean
RUN apt-get -y autoremove


### config #############################
# use workdir create dir
WORKDIR ${ARG_WORKSPACE_CONFIG}
COPY ./${ARG_RUN_ENV} ${ARG_WORKSPACE_CONFIG}


#### volume #############################
VOLUME ["${ARG_WORKSPACE_DATA}", "${ARG_CONTAINER_CODE_PATH}"]


#### expose #############################
EXPOSE 28080/tcp


#### entrypoint and cmd #############################
COPY ./entrypoint.sh /usr/bin/entrypoint.sh
ENTRYPOINT ["/usr/bin/entrypoint.sh"]
CMD ["/bin/bash"]


#### workdir #############################
WORKDIR ${ARG_CONTAINER_CODE_PATH}