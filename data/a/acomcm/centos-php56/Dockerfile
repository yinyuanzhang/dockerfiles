From centos:7

# Update packages
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm && \
  rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \
  yum update -y

# Installing php-fpm and module
RUN yum --enablerepo=remi,remi-php56 install -y php-fpm php-cli php-common \
  php-pecl-mongo php-mcrypt php-mbstring php-pdo php-xml

# COPY www.conf
COPY www.conf /etc/php-fpm.d/

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Cleanup
RUN yum clean all && rm -rf /tmp/*

EXPOSE 9000

CMD ["php-fpm", "-F"]
