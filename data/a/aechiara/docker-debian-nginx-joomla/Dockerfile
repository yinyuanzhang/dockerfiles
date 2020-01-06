from debian:jessie
MAINTAINER Alex Eduardo Chiaranda aechiara@gmail.com

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -y upgrade && \
  apt-get install -y wget nginx php5-fpm php5-mysql mysql-client && \
  apt-get clean && rm -rf /var/lib/apt/lists

RUN mkdir -p /var/www/joomla && \
	cd /var/www/joomla && \
	wget -c https://github.com/joomla/joomla-cms/releases/download/3.3.6/Joomla_3.3.6-Stable-Full_Package.tar.gz --no-check-certificate && \
	tar zxvf Joomla*.tar.gz && \
	rm -rf Joomla*.tar.gz

WORKDIR /root
ADD run.sh /root/run.sh
ADD setup.sh /root/setup.sh
ADD joomla /root/joomla
ADD mysql_setup.sql /root/mysql_setup.sql

ENV DATABASE_NAME default_db
ENV DATABASE_USER user_db
ENV DATABASE_PASSWORD pass_db

RUN /root/setup.sh

EXPOSE 80

CMD ["/root/run.sh"]
