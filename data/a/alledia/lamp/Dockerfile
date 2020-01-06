FROM phusion/baseimage

MAINTAINER Alledia <suport@alledia.com>

# Install the packages
RUN apt-get -y update \
        && apt-get install -y \
            curl \
            procps \
            unzip \
            apache2 \
            php5 \
            libicu-dev \
            mysql-server \
            libapache2-mod-php5 \
            php5-curl \
            php5-mysql \
            php5-mcrypt \
            php5-curl \
            php5-gd \
            php5-intl \
            php5-xmlrpc \
            php5-xsl \
            nano \
        && apt-get remove --purge -y vim \
        && apt-get purge -y \
        && rm -rf /var/lib/apt/lists/* \
        && apt-get clean \
        && rm -rf /tmp/* /var/tmp/* \
        && rm -rf /var/lib/apt/lists/* \
        && rm -f /etc/dpkg/dpkg.cfg.d/02apt-speedup

# Configure Apache
COPY apache/sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY apache/sites-available/000-default-ssl.conf /etc/apache2/sites-available/000-default-ssl.conf

RUN a2ensite 000-default \
    && a2ensite 000-default-ssl \
    && a2enmod substitute rewrite ssl proxy proxy_http \
    # MySQL
    && service mysql start \
    && mysqladmin -u root password root \
    # Enable SSH - For development environments only
    && rm -f /etc/service/sshd/down \
    && /etc/my_init.d/00_regen_ssh_host_keys.sh \
    && /usr/sbin/enable_insecure_key \
    # SSL
    && mkdir /etc/apache2/ssl \
    && openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout /etc/apache2/ssl/apache.key -out /etc/apache2/ssl/apache.crt -subj '/O=OSTraining/OU=Development/CN=www.ostraining.com' -batch

# Exposes the port 80
EXPOSE 80

# Exposes the volume
VOLUME ["/var/log/apache2", "/var/www/html"]

ENV TERM xterm

# Run the installer
COPY run.sh /run.sh
CMD sh /run.sh
