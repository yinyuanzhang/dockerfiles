FROM phusion/baseimage:0.9.19
MAINTAINER Adi Priyanto <adipriyanto.bpn@gmail.com>

# needed by certain software which need to save its configuration in HOME dir, eg. git
ENV HOME /root

# prepare all init scripts
COPY . /build

RUN chmod +x -R /build \
    \
# prepare package installation
    && build/common/prepare-installation.sh \
    \
# install & configure nginx
    && /build/nginx/install-packages.sh \
    && /build/nginx/setup.sh \
# install & configure php-fpm
    && /build/php-fpm/install-packages.sh \
    && /build/php-fpm/setup.sh \
# install & configure mysql
    && /build/mysql/install-packages.sh \
    && /build/mysql/setup.sh \
# install & configure ssh
    && /build/ssh/setup.sh \
    \
# clean up
    && /build/common/cleanup.sh \
    && rm -rf /build

VOLUME [ "/tmp/app" ]
VOLUME [ "/tmp/db" ]

EXPOSE 80 443 3306
