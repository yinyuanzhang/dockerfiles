FROM php:5.6-alpine3.8
MAINTAINER oldiy <oldiy2018@gmail.com>

RUN apk add git tzdata && \
	git clone https://github.com/luolongfei/freenom.git && \
	cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
	apk del tzdata git && \
	mkdir -p oldiy && \
	cp /freenom/config.php /oldiy/ && \
	rm -rf /freenom/config.php && \
	sed -i 's/smtp.gmail.com/smtp.qq.com/g' /freenom/index.php && \
	echo '00 08 * * * cd /freenom/; php index.php >/dev/null 2>&1'>>/var/spool/cron/crontabs/root

COPY start.sh /freenom/
RUN chmod +x /freenom/start.sh

VOLUME ["/conf"]
CMD ["/freenom/start.sh"]