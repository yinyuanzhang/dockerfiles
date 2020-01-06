FROM elcweb/docker-jenkins-slave-ubuntu1404-base

# Install PHP 5.5
RUN DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew"  --no-install-recommends php5 php5-cli php5-curl php5-gnupg php5-memcached php5-mysql php5-sqlite php5-mcrypt php-pear php5-xdebug &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin

RUN php5enmod mcrypt
