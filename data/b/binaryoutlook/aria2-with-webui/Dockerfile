FROM alpine:edge

MAINTAINER LaySent <laysent@gmail.com>

RUN echo 'http://mirrors.aliyun.com/alpine/edge/community/' > /etc/apk/repositories && \
	echo 'http://mirrors.aliyun.com/alpine/edge/main/' >> /etc/apk/repositories && \
  apk update && \
	apk upgrade && \
	apk add --no-cache --update bash coreutils su-exec && \
	mkdir -p /conf && \
	mkdir -p /conf-copy && \
	mkdir -p /data && \
	apk add --no-cache --update aria2 && \
	apk add git && \
	git clone https://github.com/ziahamza/webui-aria2 /aria2-webui --depth=1 && \
	rm /aria2-webui/.git* -rf && \
	apk del git && \
	apk add --update darkhttpd

ADD files/start.sh /conf-copy/start.sh
ADD files/aria2.conf /conf-copy/aria2.conf
ADD files/on-complete.sh /conf-copy/on-complete.sh

RUN chmod +x /conf-copy/start.sh

WORKDIR /
VOLUME ["/data"]
VOLUME ["/conf"]
EXPOSE 6800
EXPOSE 80
EXPOSE 8080

CMD ["/conf-copy/start.sh"]
