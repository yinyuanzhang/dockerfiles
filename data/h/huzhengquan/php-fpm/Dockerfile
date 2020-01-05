FROM ubuntu:14.04

MAINTAINER hu zhengquan "zhengquan.hu@qq.com"

RUN apt-get update && \
	apt-get install -y php5-curl php5-fpm php5-gd php5-mcrypt php5-mysql php5-pgsql php5-sqlite php5-json && \
	apt-get clean && \
	echo -n > /var/lib/apt/extended_states

ADD conf/www.conf /etc/php5/fpm/pool.d/www.conf
#COPY php-fpm.conf /usr/local/etc/

WORKDIR /var/www

EXPOSE 9000
CMD ["php5-fpm", "--nodaemonize"]
