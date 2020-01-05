FROM ppabc/dac:alpine-consul-base-3.7
LABEL maintainer="aqzt.com (ppabc@qq.com)"

    ENV ENABLE_HOSTS=TRUE \
        ENABLE_SMTP=FALSE


RUN set -x \
	&& addgroup -g 82 -S mysql \
	&& adduser -u 82 -D -S -G mysql mysql \
	&& chmod 777 /tmp

RUN apk add --update mariadb mariadb-client && rm -f /var/cache/apk/*
RUN apk --no-cache add tzdata  && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone 

ADD root /
### Networking
EXPOSE 3306

CMD ["/mariadb/startup.sh"]


