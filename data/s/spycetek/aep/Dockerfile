# Create a container based on Amazon Linux 2018.03.0 with Nginx 1.14 and PHP 7.2.
# Build command example: docker build -t "spycetek/aep:a2018.03.0-1.14-7.2-1" .

FROM amazonlinux:2018.03.0.20190514

# Prepare for package installation
RUN yum update -y

# Install Commands and Libraries
# diff: for development
# mysql57: MySQL client
# php72
# php72-fpm
# php72-cli
# php72-gd: for generating images
# php72-mbstring: for dealing with multi-byte languages
# php72-mysqlnd: for connecting to MySQL server
# php72-xml: for aws-sdk-php and unit testing
# python36: install pip for AWS Cli installation
# vim: for development
# unzip: for composer install
RUN yum install -y \
  diff \
  git \
  nginx \
  mysql57 \
  php72 \
  php72-fpm \
  php72-cli \
  php72-gd \
  php72-mbstring \
  php72-mysqlnd \
  php72-xml \
  python36 \
  unzip \
  vim \
  wget

# Update pip
RUN python36 -m pip install --upgrade pip

# Install AWS CLI tools
RUN python36 -m pip install awscli

# Install composer
RUN curl -s https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer

### Nginx Configuration
# Workaround for "/etc/init.d/nginx: line 17: /etc/sysconfig/network: No such file or directory"
RUN echo "NETWORKING=yes" > /etc/sysconfig/network

### PHP FPM Configuration
# Change execution user from apache to nginx
RUN if grep -iq "^user *=" /etc/php-fpm-7.2.d/www.conf; \
    then sed -i -E 's/^(user *=.*)$/;\1\nuser = nginx/' /etc/php-fpm-7.2.d/www.conf; \
    else echo 'user = nginx' >> /etc/php-fpm-7.2.d/www.conf; \
    fi

# Change execution group from apache to nginx
RUN if grep -iq "^group *=" /etc/php-fpm-7.2.d/www.conf; \
    then sed -i -E 's/^(group *=.*)$/;\1\ngroup = nginx/' /etc/php-fpm-7.2.d/www.conf; \
    else echo 'group = nginx' >> /etc/php-fpm-7.2.d/www.conf; \
    fi

# Enable auto start
RUN chkconfig nginx on && \
    chkconfig php-fpm-7.2 on

# Install npm for webpack, SCSS, and TypeScript
RUN curl -sL https://rpm.nodesource.com/setup_12.x | bash - && \
  yum install -y nodejs

# Install yarn for multiple package.json installation
# ref: https://yarnpkg.com/en/docs/install#debian-stable
#RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - && \
#  echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list && \
#  apt-get update && apt-get install -y yarn

RUN yum install -y gcc-c++ make && \
    curl -sL https://dl.yarnpkg.com/rpm/yarn.repo | tee /etc/yum.repos.d/yarn.repo && \
    yum install -y yarn

# Install Pear for ast and xdebug
RUN yum install -y php72-devel php7-pear

# Install ast for phan
RUN pecl7 install ast && \
    echo "extension=ast.so" > /etc/php-7.2.d/spycetek.ini

# Install and Configure xdebug
# php-xdebug: for debugging and PhpUnit coverage
RUN pecl7 install xdebug
RUN echo "zend_extension=/usr/lib64/php/7.2/modules/xdebug.so" > /etc/php-7.2.d/xdebug.ini && \
    echo "xdebug.remote_enable = 1" >> /etc/php-7.2.d/xdebug.ini && \
    echo "xdebug.remote_host = host.docker.internal" >> /etc/php-7.2.d/xdebug.ini && \
    echo "xdebug.remote_port = 9001" >> /etc/php-7.2.d/xdebug.ini

# Disable xdebug by default because it slows down processing php a lot.
# To enable, rename the file to `xdebug.ini`, then restart fpm.
RUN mv /etc/php-7.2.d/xdebug.ini /etc/php-7.2.d/xdebug.ini.disabled

COPY start_nginx_php-fpm.sh /root/start_nginx_php-fpm.sh
RUN chmod +x /root/start_nginx_php-fpm.sh
