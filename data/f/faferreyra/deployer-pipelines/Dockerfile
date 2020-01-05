FROM bitnami/php-fpm

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -q -y openssh-client \
    git

# Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') === '669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer
RUN php -r "unlink('composer-setup.php');"

# Deployer
RUN curl -LO https://deployer.org/releases/v4.3.0/deployer.phar
RUN mv deployer.phar /usr/local/bin/dep
RUN chmod +x /usr/local/bin/dep