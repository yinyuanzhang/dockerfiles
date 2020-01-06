FROM mysql/mysql-server:5.7
MAINTAINER iganari <iganari@qiita.com>

RUN yum update -y && yum -y reinstall glibc-common
RUN localedef -v -c -i ja_JP -f UTF-8 ja_JP.UTF-8; echo "";
env LANG=ja_JP.UTF-8

RUN rm -f /etc/localtime && \
    ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
