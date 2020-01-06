FROM hyalx/centos:centos6

MAINTAINER Indexyz <r18@hyalx.us>

RUN rpm -Uvh https://mirror.webtatic.com/yum/el6/latest.rpm && \
    yum install -y vixie-cron && \
    yum install -y php56w.x86_64 php56w-cli.x86_64 php56w-common.x86_64 php56w-gd.x86_64 php56w-ldap.x86_64 php56w-mbstring.x86_64 php56w-mcrypt.x86_64 php56w-mysql.x86_64 php56w-pdo.x86_64

CMD ["php"]
