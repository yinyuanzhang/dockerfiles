FROM scratch
MAINTAINER Fafan <fafan.art@gmail.com>
ADD centos-6.8.tar.xz /
ADD git-2.10.2.tar.xz /
RUN git --version
ADD php-7.0.13.tar.xz /
RUN useradd php
RUN php -v
RUN php -c /usr/local/lib/opcache.ini -v
RUN php -c /usr/local/lib/xdebug.ini -v
RUN php --ini
CMD /bin/bash
