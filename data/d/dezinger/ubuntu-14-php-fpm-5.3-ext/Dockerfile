FROM dezinger/ubuntu-14-php-fpm-5.3:latest

MAINTAINER dezinger@gmail.com

ENV DEBIAN_FRONTEND noninteractive

COPY files/ /
WORKDIR /var/www

RUN \
    apt-get -y update && \
# setup utils
    apt-get install --no-install-recommends -y \
    wkhtmltopdf xvfb && \
# configure    
    chmod a+x /usr/bin/wkhtmltopdf.sh && \
    ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf && \
# clean 
    apt-get -y autoremove && apt-get -y clean && apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*