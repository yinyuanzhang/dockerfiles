FROM java:8-jre-alpine

RUN apk update \
	&& apk add -U tzdata \
	&& cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
	&&  apk del tzdata
