FROM atws/c9-docker-images
MAINTAINER Cloud9 IDE, inc. <info@c9.io>

ADD ./files/home /home/ubuntu

RUN bash -c 'chmod -R g+w /home/ubuntu/{workspace,sessions} && \
    chown -R ubuntu:ubuntu /home/ubuntu/{workspace,sessions}'

# Enable the Docker container to communicate with AWS Cloud9 by
# installing SSH.
RUN apt-get update && apt-get install -y openssh-server

# Ensure that Node.js is installed.
RUN apt-get install -y nodejs 

# Disable password authentication by turning off the
# Pluggable Authentication Module (PAM).
RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config

# PHP based on defaults from
#   http://docs.travis-ci.com/user/ci-environment/#Extensions
#   https://devcenter.heroku.com/articles/php-support
# Xdebug, most recent PECL version
ADD ./files/etc/php/7.2 /etc/php/7.2
RUN apt-get update || apt-get update
RUN apt-get install -y php php-cli php-fpm \
        php-curl php-gd php-json php-pgsql php-readline \
        php-tidy php-xmlrpc php-xsl php-intl php-mysqlnd \
        php-pear php-soap \
    && apt-get install -y php-dev libmcrypt-dev php-pear \
        && pecl install xdebug \
        && phpenmod xdebug \
    && apt-get install -y python-dev \
    && pecl channel-update pecl.php.net \
    && pecl install mcrypt-1.0.1 \
    && cd /etc/php/7.2/mods-available && ls *.ini | sed 's/\.ini$//' | xargs phpenmod

RUN mkdir -p /var/run/sshd

RUN pip install -U virtualenv && \
    virtualenv --python=python2 /home/ubuntu/workspace/.c9/python2 && \
    bash /home/ubuntu/workspace/.c9/python2/bin/activate

RUN mkdir /tmp/codeintel && \
    pip download -d /tmp/codeintel codeintel==0.9.3 && \
    cd /tmp/codeintel && \
    tar -xf CodeIntel-0.9.3.tar.gz && \
    mv CodeIntel-0.9.3/SilverCity CodeIntel-0.9.3/silvercity && \
    tar -czf CodeIntel-0.9.3.tar.gz CodeIntel-0.9.3 && \
    pip install -U --no-index --find-links=/tmp/codeintel codeintel

# Start SSH in the Docker container.
CMD /usr/sbin/sshd -D

# Update the password to a random one for the user ubuntu.
RUN echo "ubuntu:$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)" | chpasswd

RUN chown -R ubuntu: /home/ubuntu/lib

ADD ./files/check-environment /.check-environment/php
