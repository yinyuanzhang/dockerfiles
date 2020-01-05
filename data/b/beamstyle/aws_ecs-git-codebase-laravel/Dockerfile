FROM beamstyle/aws_ecs-git
MAINTAINER Thomas Cheng <thomas@beamstyle.com.hk>

# Install some basic dependencies
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    lsb-release \
    ca-certificates \
    curl \
    git \
    zip \
    unzip \
    wget

# Install packages.
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php7.3.list

RUN apt-get update && apt-get install -y \
    libapache2-mod-php7.3 \
    php7.3 \
    php7.3-cli \
    php7.3-fpm \
    php7.3-json \
    php7.3-pdo \
    php7.3-mysql \
    php7.3-zip \
    php7.3-gd \
    php7.3-mbstring \
    php7.3-curl \
    php7.3-xml \
    php7.3-bcmath \
    php7.3-common \
    php7.3-sqlite3 \
    php-pear \
    php7.3-gmp \
    php7.3-intl \
    php7.3-imap \
    php7.3-ldap \
    php7.3-mysqlnd \
    php7.3-ps \
    php7.3-readline \
    php7.3-tidy \
    php7.3-xmlrpc \
    php7.3-xsl \
    php7.3-cgi \
    cron \
    gettext \
    pdftk \
    && apt-get --purge autoremove

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
ADD auth.json /tmp/auth.json

ENTRYPOINT ["sh", "-c"]

# Running the custom script file "run.sh"
ADD run.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/run.sh

CMD ["/usr/local/bin/run.sh"]
