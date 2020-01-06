FROM debian:9

MAINTAINER Ellkinox <ilyes-litim@utopiascript.fr>

ENV	DEBIAN_FRONTEND noninteractive

RUN apt-get update

RUN apt-get -y install dialog apt-utils wget nano sudo git ifupdown net-tools gnupg2 build-essential debhelper

RUN apt-get -y install ca-certificates apt-transport-https \
    && wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg \
    && echo "deb https://packages.sury.org/php/ stretch main" > /etc/apt/sources.list.d/php.list \
    && wget http://www.webmin.com/jcameron-key.asc -qO - | apt-key add - \
    && wget http://software.virtualmin.com/lib/RPM-GPG-KEY-virtualmin-6 -qO - | apt-key add -

RUN rm /etc/apt/apt.conf.d/docker-gzip-indexes \
    && apt-get purge apt-show-versions

RUN apt-get -o Acquire::GzipIndexes=false update \
    && apt-get -y install apt-show-versions \
    && apt-get update \
    && apt-get upgrade -y

CMD ["bash"]