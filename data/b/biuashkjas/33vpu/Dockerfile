# Use Alpine Linux
FROM alpine:3.4

# Declare maintainer
MAINTAINER Muhammad Zamroni <halo@matriphe.com>

# Timezone test
#test

ENV TIMEZONE Asia/Shanghai

RUN	apk update && \
	apk add  tzdata curl bash openvpn && \
	cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
	echo "${TIMEZONE}" > /etc/timezone && \
	mkdir /data && \
	apk del tzdata && \
	rm -rf /var/cache/apk/*


#COPY conf/auth.log /data/auth.log

COPY conf /data

#COPY conf/ss.json   /data/ss.json

COPY conf/sss       /usr/bin/sss
COPY conf/cron.log  /var/spool/cron/crontabs/root
RUN chmod +x /data/run.sh
RUN chmod +x /usr/bin/sss


EXPOSE 8091
VOLUME ["/data"]

#CMD ["/data/run.sh && tail -f"]
CMD /data/run.sh && tail -f