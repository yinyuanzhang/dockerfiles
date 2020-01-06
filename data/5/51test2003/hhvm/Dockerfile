FROM ubuntu:14.04 

# 签名啦
MAINTAINER yongboy "51test2003@163.com"

RUN apt-get install -y nginx

RUN apt-get install -y software-properties-common && \
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0x5a16e7281be7a449 && \
add-apt-repository 'deb http://mirrors.hypo.cn/hhvm/ubuntu trusty main' && \
apt-get update -y && \
apt-get install -y hhvm && \
/usr/share/hhvm/install_fastcgi.sh && \
update-rc.d hhvm defaults

EXPOSE 80

VOLUME /var/lib/hhvm

