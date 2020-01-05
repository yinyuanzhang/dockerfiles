FROM aune/cloud9:latest

# Install Apache and PHP
RUN apt-get update ; \
    apt-get -y install mysql-client redis ; \
    apt-get -y install software-properties-common ; \
    add-apt-repository ppa:ondrej/php ; \
    DEBIAN_FRONTEND=noninteractive apt-get -y install php7.3 php7.3-mysql php7.3-mbstring php7.3-curl php7.3-xml php7.3-bcmath php7.3-gd php7.3-intl php7.3-soap php7.3-zip php7.3-cli libapache2-mod-php7.3 ; \
    apt-get autoclean ; \
    apt-get clean

RUN a2enmod rewrite

# Install composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" ; \
    php -r "if (hash_file('sha384', 'composer-setup.php') === 'a5c698ffe4b8e849a443b120cd5ba38043260d5c4023dbf93e1558871f1f07f58274fc6f4c93bcfd858c6bd0775cd8d1') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" ; \
    php composer-setup.php ; \
    php -r "unlink('composer-setup.php');" ; \
    mv composer.phar /usr/local/bin/composer
