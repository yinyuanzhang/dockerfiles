FROM circleci/php:5.6-apache-node-browsers
MAINTAINER Josh Rose josh.rose_at_civicactions.com

# Install Selenium
RUN sudo npm install selenium-standalone@latest -g && \
    sudo selenium-standalone install

# Additional Packages.
RUN sudo apt-get update && sudo apt-get install -y ruby libpng-dev libmcrypt-dev mysql-client x11vnc

# Install PHP Extensions
#Available Extensions:
#bcmath bz2 calendar ctype curl dba dom enchant exif fileinfo filter ftp gd gettext gmp hash iconv imap interbase intl json ldap mbstring mcrypt mssql mysql mysqli oci8 odbc opcache pcntl pdo pdo_dblib pdo_firebird pdo_mysql pdo_oci pdo_odbc pdo_pgsql pdo_sqlite pgsql phar posix pspell readline recode reflection session shmop simplexml snmp soap sockets spl standard sybase_ct sysvmsg sysvsem sysvshm tidy tokenizer wddx xml xmlreader xmlrpc xmlwriter xsl zip
RUN sudo docker-php-ext-install gd json mcrypt mysql mysqli opcache pdo pdo_mysql zip

# Additional MySQL Configuration
RUN sudo chmod 777 /etc/mysql/my.cnf && \
    sudo echo -e "[client]\nloose-local-infile" >> /etc/mysql/my.cnf && \
    sudo chmod 644 /etc/mysql/my.cnf

# Additional PHP Configuration
RUN sudo chmod 777 /usr/local/etc/php/conf.d && \
    sudo echo "memory_limit = 512M" > /usr/local/etc/php/conf.d/memory.ini && \
    sudo echo "always_populate_raw_post_data = -1" > /usr/local/etc/php/conf.d/deprecated.ini && \
    sudo chmod 755 /usr/local/etc/php/conf.d

# Install Ahoy
RUN sudo wget -q https://github.com/devinci-code/ahoy/releases/download/1.1.0/ahoy-`uname -s`-amd64 -O /usr/local/bin/ahoy && \
            sudo chmod +x /usr/local/bin/ahoy

