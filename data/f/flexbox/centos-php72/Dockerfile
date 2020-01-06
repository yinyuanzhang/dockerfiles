FROM centos/systemd

LABEL name="Flexbox CentOS 7.4 + PHP 7.2 Image" \
    maintainer="Alex Karshin <https://flexbox.it>" \
    license="The Unlicense" \
    build-date="20180512" \
    source="https://github.com/flexbox-it/dockerimage-centos-php7"

# update yum
RUN yum clean all; yum -y update --nogpgcheck
RUN yum -y install yum-utils

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm; \
    rpm -Uvh http://rpms.remirepo.net/enterprise/remi-release-7.rpm; \
    yum-config-manager --enable remi-php72

# Install some must-haves
RUN yum -y install --nogpgcheck \
    epel-release \
    wget \
    git \
    nano \
    postfix \
    gcc-c++ \
    make

RUN yum -y install \
    php \
    php-bcmath \
    php-cli \
    php-curl \
    php-devel \
    php-gd \
    php-fpm \
    php-imagick \
    php-intl \
    php-mbstring \
    php-mcrypt \
    php-mysqlnd \
    php-opcache --nogpgcheck \
    php-pdo \
    php-posix \
    php-xml \
    php-zip

RUN curl https://phar.phpunit.de/phpunit.phar -L -o phpunit.phar && \
    chmod +x phpunit.phar && \
    mv phpunit.phar /usr/local/bin/phpunit

RUN rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm
RUN yum -y install nginx --nogpgcheck

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt. Maybe a new version was released and you forgot to update the verification hash?'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    mv composer.phar /usr/local/bin/composer

RUN curl --silent --location https://rpm.nodesource.com/setup_9.x | bash - && \
    yum -y install nodejs

RUN mkdir -p /tmp
RUN mkdir -p /run/php-fpm
RUN chown -R nginx:nginx /var/lib/php/session && chmod 0777 /var/lib/php/session

COPY start.sh /tmp/start.sh
COPY php/memory.ini /etc/php.d/01-memory.ini
COPY php/datetime.ini /etc/php.d/01-datetime.ini
COPY php/session.ini /etc/php.d/01-session.ini
COPY php/www.conf /etc/php-fpm.d/www.conf
COPY postfix/main.cf /etc/postfix/main.cf
COPY postfix/main.cf.working /etc/postfix/main.cf.working

WORKDIR "/html"

EXPOSE 80 443

ARG user=1000
ARG group=1000

RUN usermod -u $user nginx
RUN groupmod -g $group nginx

CMD ["/tmp/start.sh"]
