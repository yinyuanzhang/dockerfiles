##############################################################################
# Install ubuntu 14.04.5
##############################################################################

FROM ubuntu:14.04.5

##############################################################################
# This forces the image to be build on every push!
##############################################################################

ARG CACHEBUST=0

##############################################################################
# Install fixed apache2
##############################################################################

RUN apt-get update --fix-missing && \
	apt-get install -y software-properties-common && \
	locale-gen en_US.UTF-8 && \
	LANG=en_US.UTF-8 add-apt-repository -y ppa:ondrej/apache2 && \
	apt update && \
	apt install -y apache2 apache2-dev build-essential autoconf make libtool libssl-dev libjansson-dev libcurl4-openssl-dev && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

##############################################################################
# Install mod_md
##############################################################################

ADD https://github.com/icing/mod_md/releases/download/v1.1.16/mod_md-1.1.16.tar.gz /tmp/

# Needed by `a2enmod md`, thus we copy them before we build mod_md
COPY etc/apache2/mods-available/md.load /etc/apache2/mods-available/
COPY etc/apache2/mods-available/md.conf /etc/apache2/mods-available/

RUN cd /tmp/ && \
    tar -zxvf mod_md-1.1.16.tar.gz && \
    cd /tmp/mod_md-1.1.16 && \
    ./configure --with-apxs=/usr/bin/apxs && \
    make && \
    make install && \
    a2enmod ssl md

##############################################################################
# Startup apache2
##############################################################################

EXPOSE 80
CMD apachectl -D FOREGROUND
