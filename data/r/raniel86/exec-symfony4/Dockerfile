FROM centos

# system preparation
RUN yum update -y
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm
RUN yum install -y yum-utils
RUN yum-config-manager --enable remi-php72
RUN yum install -y unzip php php-mcrypt php-cli php-gd php-curl php-mysql php-ldap php-zip php-fileinfo php-xml php-mbstring git

# install composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/bin/composer

# set variables
ENV DIR /app
ENV PORT 8888

# run symfony4 application
EXPOSE $PORT
COPY ./app $DIR
WORKDIR $DIR
CMD ["sh", "-c", "php -S 0.0.0.0:${PORT} -t public"]
