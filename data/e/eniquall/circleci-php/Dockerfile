FROM ubuntu:16.04
MAINTAINER eniquall <eniquall@gmail.com>

## Ask nothing when install with apt or deb
ENV DEBIAN_FRONTEND noninteractive


RUN apt-get clean && apt-get -y update && apt-get install -y locales curl software-properties-common git \
  && locale-gen en_US.UTF-8

# set default locale
RUN sh -c 'echo "LC_ALL=en_US.UTF-8" >> /etc/default/locale' \
    sh -c 'echo "LANG=en_US.UTF-8" >> /etc/default/locale'

RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php
RUN apt-get update && apt-get install -y php-zip php-xml php-soap php-gd php-curl php-intl php-mysql php-snmp \
    php-imap php-imagick php-mcrypt php-mbstring php-dev \
    snmp libpcre3 libpcre3-dev libssl-dev zlib1g-dev unzip git

# install font-pack for asian fonts
RUN apt-get -y install language-pack-zh-hans fonts-arphic-uming ttf-dejavu ttf-wqy-microhei \
    && fc-cache -f -v
    
RUN apt-get -y install nginx

# install php-gmp extention
RUN apt-get install php7.1-gmp

RUN echo '\n\
short_open_tag = On \n\
error_log = syslog \n\
post_max_size=20M \n\
upload_max_filesize=20M \n\
max_execution_time=300 \n\
max_input_time=300 \n\
date.timezone=UTC \n\
display_errors = On \n\
display_startup_errors = On \n\
expose_php = Off \n\
max_input_vars = 2000 \n\
\n\
extension=timecop.so \
' >> /etc/php/7.1/cli/php.ini


RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer

RUN cd /tmp \
    && git clone https://github.com/hnw/php-timecop.git \
    && cd php-timecop \
    && phpize \
    && ./configure \
    && make \
    && make install

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*