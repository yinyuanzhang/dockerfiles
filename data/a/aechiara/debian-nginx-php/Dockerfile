from debian:jessie
MAINTAINER Alex Eduardo Chiaranda aechiara@gmail.com

ENV DEBIAN_FRONTEND noninteractive

RUN mkdir -p /var/www/website && \
  apt-get update && apt-get -y upgrade && \
  apt-get install -y wget nginx php5-fpm php5-mysql mysql-client && \
  apt-get clean && rm -rf /var/lib/apt/lists

WORKDIR /root
ADD run.sh /root/run.sh
ADD setup.sh /root/setup.sh
ADD nginx-default /root/nginx-default
ADD mysql_setup.sql /root/mysql_setup.sql

ENV DATABASE_NAME default_db
ENV DATABASE_USER user_db
ENV DATABASE_PASSWORD pass_db

RUN /root/setup.sh

EXPOSE 80

CMD ["/root/run.sh"]
