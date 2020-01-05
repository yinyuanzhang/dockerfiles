FROM debian:stretch-slim
MAINTAINER Rómulo Rodríguez rodriguezrjrr@gmail.com

# Update system and install
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y \
        apache2 \
        libapache2-mod-php7.0 \
        net-tools \
        php7.0 \
        php7.0-apcu \
        php7.0-bcmath \
        php7.0-bz2 \
        php7.0-curl \
        php7.0-gd \
        php7.0-geoip \
        php7.0-gnupg \
        php7.0-imagick \
        php7.0-imap \
        php7.0-intl \
        php7.0-json \
        php7.0-ldap \
        php7.0-mcrypt \
        php7.0-mongodb \
        php7.0-msgpack \
        php7.0-mysql \
        php7.0-odbc \
        php7.0-pgsql \
        php7.0-soap \
        php7.0-sqlite \
        php7.0-sybase \
        php7.0-xsl \
        php7.0-zip \
        wget \
    && apt-get autoremove -y \
    && apt-get clean -y

RUN apt-get update -y \
    && apt-get install -y \
        build-essential apache2-dev \
    && wget https://github.com/gnif/mod_rpaf/archive/v0.8.4.tar.gz \
    && tar -xzf v0.8.4.tar.gz \
    && cd mod_rpaf-0.8.4 \
    && make \
    && make install \
    && apt-get remove -y build-essential apache2-dev \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && echo "LoadModule rpaf_module /usr/lib/apache2/modules/mod_rpaf.so" > /etc/apache2/mods-available/rpaf.load

ADD magic_quotes.ini /etc/php/7.0/mods-available
ADD rpaf.conf /etc/apache2/mods-available/

RUN phpenmod magic_quotes \
    && a2enmod expires \
    && a2enmod rewrite \
    && a2enmod filter \
    && a2enmod deflate \
    && a2enmod rpaf \
    && ln -sfT /dev/stderr "/var/log/apache2/error.log" \
    && ln -sfT /dev/stdout "/var/log/apache2/access.log" \
    && sed -i "s/^Listen 80\$/Listen 8080/" /etc/apache2/ports.conf

ENV PROCESSMAKER_RELEASE 3.3.10
ENV PROCESSMAKER_TARGZ "/opt/processmaker-$PROCESSMAKER_RELEASE-community.tar.gz"
RUN wget -O $PROCESSMAKER_TARGZ \
      "https://sourceforge.net/projects/processmaker/files/ProcessMaker/$PROCESSMAKER_RELEASE/processmaker-$PROCESSMAKER_RELEASE-community.tar.gz/download" \
    && mkdir /opt/processmaker

# COPY processmaker-3.3.10-community.tar.gz /opt
# RUN mkdir /opt/processmaker

ADD entrypoint.sh /usr/bin/entrypoint.sh
ADD 000-default.conf /etc/apache2/sites-available/000-default.conf

RUN chmod -R g+w \
        /etc/php/7.0/apache2 \
        /etc/php/7.0/apache2/php.ini \
        /etc/php/7.0/cli \
        /etc/php/7.0/cli/php.ini \
        /run/apache2 \
        /var/log/apache2 \
        /opt/processmaker \
    && chmod +x /usr/bin/entrypoint.sh \
    && chown -R root:root /var/log/apache2

EXPOSE 8080
VOLUME /opt/processmaker
ENTRYPOINT ["entrypoint.sh"]
