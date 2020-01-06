FROM lunalabs/ubuntu18

#install php7.2 and dependecies
USER root
RUN apt-get update && \
apt-get upgrade && \
apt-get install -y php7.2 \
libapache2-mod-php7.2 \
php7.2-xml \
php7.2-mbstring \
php7.2-mysql \
php7.2-json \
php7.2-curl \
php7.2-cli \
php7.2-common \
php-apcu \
php-pear \
php7.2-gd \
libapache2-mod-php7.2 \
php7.2-zip \
php-mailparse \
php-soap \
sendmail \
cmake \
libpng-dev \
composer && \
apt-get autoremove

RUN mkdir -p -m777 /sorgenti && chown www-data:www-data /sorgenti

# install node 8.x
USER root
WORKDIR /sorgenti
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install -y nodejs

# install zint (barcode generator)
USER root
RUN mkdir -p /tmp/zint
WORKDIR /tmp/zint
RUN wget https://sourceforge.net/projects/zint/files/zint/2.6.3/zint-2.6.3_final.tar.gz && tar xvf zint-2.6.3_final.tar.gz
WORKDIR /tmp/zint/zint-2.6.3.src
RUN cmake .
RUN make && make install
