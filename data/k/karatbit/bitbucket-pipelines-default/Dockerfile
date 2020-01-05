FROM ubuntu:18.04

MAINTAINER Florin Motoc <dev@mflorin.com>

# Set environment variables
ENV HOME /root

# MySQL root password
ARG MYSQL_ROOT_PASS=root

# Cloudflare DNS
RUN echo "nameserver 1.1.1.1" | tee /etc/resolv.conf > /dev/null

# Install packages
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    git \
    unzip \
    mcrypt \
    wget \
    curl \
    openssl \
    ssh \
    locales \
    less \
    composer \
    sudo \
    mysql-server \
    npm \
    php-pear php7.2-mysql php7.2-zip php7.2-xml php7.2-mbstring php7.2-curl php7.2-json php7.2-pdo php7.2-tokenizer php7.2-cli php7.2-imap php7.2-intl php7.2-gd php7.2-xdebug php7.2-soap php7.2-bcmath php7.2-sqlite3 \
    --no-install-recommends && \
    apt-get clean -y && \
    apt-get autoremove -y && \
    apt-get autoclean -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    rm /var/lib/mysql/ib_logfile*

# Ensure UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8
RUN locale-gen en_US.UTF-8

# Timezone
RUN echo "date.timezone=UTC" > /etc/php/7.2/cli/conf.d/date_timezone.ini

# Goto temporary directory.
WORKDIR /tmp
