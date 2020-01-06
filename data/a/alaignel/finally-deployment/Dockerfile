FROM centos:7
ENTRYPOINT ["/usr/sbin/init"]
CMD ["systemctl"]
ENV TZ=GMT

# Other
RUN mkdir /root/.ssh
ADD id_rsa /root/.ssh
ADD id_rsa.pub /root/.ssh

RUN chmod 600 /root/.ssh/id_rsa
RUN chmod 644 /root/.ssh/id_rsa.pub

# RUN export LC_ALL=C.UTF-8
# RUN DEBIAN_FRONTEND=noninteractive
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN yum install -y wget

RUN wget http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
RUN rpm -ivh epel-release-latest-7.noarch.rpm
RUN yum repolist

RUN yum update -y
RUN yum install -y \
    sudo \
    autoconf \
    autogen \
    language-pack-en-base \
    wget \
    zip \
    unzip \
    curl \
    rsync \
    ssh \
    openssh-client \
    git \
    build-essential \
    apt-utils \
    software-properties-common \
    nasm \
    mysql \
    mysql-server \
    mysql-devel \
    pngquant \
    libjpeg-dev \
    libpng-dev \
    libpng16-16
    
# Test
# RUN pngquant -v

# MySQL Setup
RUN cd /tmp/
RUN wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm && rpm -ivh mysql-community-release-el7-5.noarch.rpm
RUN yum -y update
RUN yum -y install mysql

#RUN mysql_install_db --user=mysql --datadir=/var/lib/mysql
#RUN su mysql -c /usr/bin/mysqld_safe &
#RUN /usr/bin/mysqladmin -u root password 'root'

# RUN systemctl start mysqld
# RUN mysql -v
# RUN mysqladmin -u root password ‘root’
    
# Node 
RUN sudo curl -sL https://rpm.nodesource.com/setup_10.x | bash -
RUN sudo yum -y --enablerepo=nodesource install nodejs
# Nodesource nodejs includes node
# RUN sudo yum -y --enablerepo=nodesource install npm
RUN command -v node
RUN command -v npm

RUN useradd -m docker
# RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

# PHP
RUN sudo yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm 
RUN sudo yum -y install epel-release yum-utils
RUN sudo yum-config-manager --disable remi-php54
RUN sudo yum-config-manager --enable remi-php73
RUN sudo yum -y install php php-cli php-fpm php-mysqlnd php-zip php-devel php-gd php-mcrypt php-mbstring php-curl php-xml php-pear php-bcmath php-json
RUN command -v php

# Composer
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer && \
    chmod +x /usr/local/bin/composer && \
    composer self-update --preview
RUN command -v composer

# PHPUnit
RUN wget https://phar.phpunit.de/phpunit.phar
RUN chmod +x phpunit.phar
RUN mv phpunit.phar /usr/local/bin/phpunit
RUN command -v phpunit

# Node.js
RUN sudo yum -y install epel-release
RUN sudo yum -y install git-lfs
RUN sudo git lfs install

# Deps
RUN sudo yum -y install libpng-devel
RUN npm -g install yarn
RUN npm -g --unsafe-perm install node-sass

# Display versions installed
RUN php -v
RUN composer --version
RUN phpunit --version
RUN node -v
RUN npm -v
