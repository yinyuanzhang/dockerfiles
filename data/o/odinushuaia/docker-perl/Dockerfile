FROM frolvlad/alpine-glibc

MAINTAINER Liu Yiding<odinushuaia@gmail.com>

# install perl
RUN apk update
RUN apk add perl perl-dev gcc g++ make mariadb-dev bash

# basic package
RUN perl -MCPAN -e 'install DBI'
RUN perl -MCPAN -e 'install DBD::mysql'

# clean rubbish
RUN apk del gcc g++ make
RUN rm -rf /usr/lib/lib*.a

RUN sed -ie 's/dl-cdn.alpinelinux.org/mirror.tuna.tsinghua.edu.cn/g' /etc/apk/repositories
RUN mkdir -p /root/.cpan/CPAN/
COPY MyConfig.pm /root/.cpan/CPAN/
