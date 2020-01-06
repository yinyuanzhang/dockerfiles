FROM ubuntu:latest

LABEL maintainer "itiQiti SAS <opensource@itiqiti.com>"

ENV MODE=default \
    DEV_PACKAGES="build-essential sudo man curl htop wget lsb-release apt-utils apt-transport-https git tmux ssh vim" \
    DEV_PHP_PACKAGES="php7.0 php7.0-curl php7.0-json php7.0-cgi php7.0-fpm autoconf automake libxml2-dev libcurl4-openssl-dev libssl-dev openssl gettext libicu-dev libmcrypt-dev libmcrypt4 libbz2-dev libreadline-dev gettext build-essential libmhash-dev libmhash2 libicu-dev libxslt-dev pkg-config libssl-dev libzmq3-dev" \
    DEV_DKCONF_VERSION="0.2" \
    DEV_HUB_VERSION="2.3.0-pre10" \
    DEV_TMUX_VERSION="2.5" \
    DEV_COMPOSER_VERSION="master" \
    DEV_NVM_VERSION="latest" \
    DEV_PHPBREW_VERSION="master" \
    DEV_PHPBREW_PHP_CURRENT_VERSION="5.6.31" \
    DEV_PHPBREW_PHP_NEW_VERSION="7.1.9" \
    DEV_NVM_CURRENT_VERSION="4" \
    DEV_NVM_NEW_VERSION="stable" \
    DEV_USER_GROUP="developer-group" \
    DEV_USER_GID=1000

ARG DONT_POPULATE_VERSIONS=0

RUN apt update && apt install -y $DEV_PACKAGES $DEV_PHP_PACKAGES
RUN mkdir -p /apps
RUN echo "[Tools] Install DKConf $DEV_DKCONF_VERSION ..." && \
    curl -s -f -L https://github.com/itiqiti/dkconf/releases/download/$DEV_DKCONF_VERSION/dkconf-linux -o /usr/local/bin/dkconf && \
    chmod +x /usr/local/bin/dkconf
RUN echo "[Tools] Install HUB $DEV_HUB_VERSION ..." && \
    curl -s -f -L https://github.com/github/hub/releases/download/v$DEV_HUB_VERSION/hub-linux-amd64-$DEV_HUB_VERSION.tgz -o /tmp/hub.tgz && \
    cd /tmp && tar xzvf /tmp/hub.tgz > /dev/null && cp hub-*-$DEV_HUB_VERSION/bin/hub /usr/local/bin/hub && \
    chmod +x /usr/local/bin/hub
RUN echo "[Tools] Install PHPBrew $DEV_PHPBREW_VERSION ..." && \
    curl -s -f -L https://github.com/phpbrew/phpbrew/raw/$DEV_PHPBREW_VERSION/phpbrew -o /usr/local/bin/phpbrew && \
    chmod +x /usr/local/bin/phpbrew
RUN echo "[[ -e ~/.phpbrew/bashrc ]] && source ~/.phpbrew/bashrc" >> ~/.bashrc && \
    bash -c "phpbrew init" && \
    echo "export PHPBREW_ROOT=/opt/phpbrew" >> ~/.phpbrew/bashrc && \
    echo "export PHPBREW_HOME=/root/.phpbrew " >> ~/.phpbrew/bashrc && \
    mkdir /etc/skel/.phpbrew && cp ~/.phpbrew/bashrc /etc/skel/.phpbrew/ && \
    bash -c "source ~/.phpbrew/bashrc && phpbrew update && phpbrew known && phpbrew variants" && \
    bash -c "source ~/.phpbrew/bashrc && [[ $DONT_POPULATE_VERSIONS -eq 1 ]] || (phpbrew install $DEV_PHPBREW_PHP_CURRENT_VERSION +default && phpbrew install $DEV_PHPBREW_PHP_NEW_VERSION +default && phpbrew switch $DEV_PHPBREW_PHP_CURRENT_VERSION)" && \
    bash -c "source ~/.phpbrew/bashrc && [[ $DONT_POPULATE_VERSIONS -eq 1 ]] || (phpbrew ext install xdebug stable && phpbrew ext install mongo && phpbrew ext install zmq beta && phpbrew ext install redis)"
RUN echo "[Tools] Install Composer $DEV_COMPOSER_VERSION ..." && \
    wget https://raw.githubusercontent.com/composer/getcomposer.org/$DEV_COMPOSER_VERSION/web/installer -O - -q | php -- --quiet && \
    mv composer.phar /usr/local/bin/composer && \
    chmod +x /usr/local/bin/composer
RUN echo "[Tools] Install NVM $DEV_NVM_VERSION ..." && \
    git clone https://github.com/creationix/nvm.git /opt/nvm &&\
    mkdir /usr/local/nvm && \
    echo "export NVM_DIR=/usr/local/nvm" > /etc/profile.d/nvm.sh && \
    echo "source /opt/nvm/nvm.sh" >> /etc/profile.d/nvm.sh && \
    echo "export PATH=\"/usr/local/node/bin:\$PATH\"" >> /etc/profile.d/nvm.sh && \
    bash -c "source /etc/profile.d/nvm.sh && [[ $DONT_POPULATE_VERSIONS -eq 1 ]] || (nvm install $DEV_NVM_CURRENT_VERSION && nvm install $DEV_NVM_NEW_VERSION && nvm alias default $DEV_NVM_NEW_VERSION)" && \
    true

ENV DEV_CHOWN_DIRS="/usr/local/nvm /opt/phpbrew" \
    DEV_CUSTOM_PACKAGES=""

RUN apt install -y $DEV_CUSTOM_PACKAGES

RUN addgroup -gid $DEV_USER_GID $DEV_USER_GROUP && \
    chown -R :$DEV_USER_GROUP $DEV_CHOWN_DIRS && \
    chmod -R g=u $DEV_CHOWN_DIRS

COPY ["docker-entrypoint.sh", "/usr/local/bin/"]
COPY [".bashrc", "/tmp/bashrc"]

WORKDIR /apps/

ENTRYPOINT ["docker-entrypoint.sh"]

CMD  ["/bin/bash" ]
