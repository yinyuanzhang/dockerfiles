FROM alpine:latest
LABEL MAINTAINER="Greg Junge <gregnuj@gmail.com>"
USER root

# To enable build behind proxy
ARG http_proxy

# Install packages
RUN set -ex \
    && apk add --no-cache \
    bash \
    bind-tools \
    busybox-extras \
    busybox-suid \
    curl \
    dcron \
    gettext \
    git \
    grep \
    less \
    libice \
    libsm \
    libx11 \
    libxt \
    msmtp \
    ncurses \
    nmap \
    nodejs \
    openjdk8 \
    openssl \
    openssh \
    php7 \
    php7-json \
    rsync \
    socat \
    sudo \
    supervisor \
    unzip \
    vim \
    wget \
    yarn 

# add files in rootfs
ADD ./rootfs /

# Set Root to bash not ash and overwrite .bashrc
RUN set -ex \
    && sed -i 's/root:\/bin\/ash/root:\/bin\/bash/' /etc/passwd \
    && cp /etc/skel/.bashrc /root/.bashrc \
    && chmod 4755 /usr/bin/crontab \
    && mkdir -p /var/log/supervisord \
    && mkdir -p /var/run/sshd \
    && mkdir -p /var/log/msmtp \
    && if [ -e /usr/sbin/sendmail ]; then rm -f /usr/sbin/sendmail; fi \
    && ln -s /usr/bin/msmtp /usr/sbin/sendmail \
    && if [ -e /var/www/html ]; then rm -rf /var/www/html; fi \
    && mkdir -p /var/www/localhost/htdocs \
    && ln -s /var/www/localhost/htdocs /var/www/html \
    && git config --global credential.helper store

# Setup environment
    ENV SHELL="/bin/bash" \
    EDITOR="/usr/bin/vim" \
    # defaults to 'cyclops'
    APP_USER=""  \ 
    # defaults to random
    APP_PASSWD=""  \ 
    # defaults to 10000
    APP_UID="" \
    # defaults to $APP_USER
    APP_GROUP="" \ 
    # defaults to $APP_USER
    APP_SUDO=""  \ 
    # defaults to $APP_UID
    APP_GID=""   \ 
    # defaults to /home/$APP_USER
    APP_HOME=""  \ 
    # defaults to /home/$APP_USER/.ssh
    APP_SSH=""   \ 
    # defaults to /home/$APP_USER/.ssh
    APP_TYPE=""   \ 
    # defaults to /home/$APP_USER/.ssh/id_rsa
    APP_KEY=""   \ 
    # defaults to /home/$APP_USER/.ssh/authorized_keys
    APP_AUTH="" \
    # install adminer
    HTDOCS_DIR="/var/www/localhost/htdocs" \   
    # install adminer
    ADMINER_INSTALL="" \
    ADMINER_DIR="/var/www/localhost/htdocs/adminer" \
    # install codiad
    CODIAD_INSTALL="" \
    CODIAD_DIR="/var/www/localhost/htdocs/codiad" \
    # install webconsole
    WEBCONSOLE_INSTALL="" \
    WEBCONSOLE_DIR="/var/www/localhost/htdocs/webconsole" \
    # used in some scripts
    SSH_PORT="22" \   
    DATA_PORT="3306" \   
    WEB_PORT="80" \    
    CRON_OPTS=""

EXPOSE 22 8000 9001
VOLUME ["/var/www/localhost/htdocs"]
WORKDIR "/var/www/localhost/htdocs"
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]
