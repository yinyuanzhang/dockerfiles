FROM awhalen/docker-php-composer-node
MAINTAINER fdsze <freddie@y714.com>

# setup workdir
RUN mkdir -p /root/work/
WORKDIR /root/work/

# install git
RUN apt-get -y update && apt-get -y install git && apt-get -y install lftp && apt-get -y install git-ftp

# slim down image
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/?? /usr/share/man/??_*

# configure the image to send insecure requests regardless of the ftp server ssl
# RUN git config git-ftp.insecure 1
