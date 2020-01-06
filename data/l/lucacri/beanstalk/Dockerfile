FROM alpine:latest


COPY rootfs /

# Download and build beanstalk
RUN buildDeps='gcc curl musl-dev make tar netcat-openbsd' \
	BEANSTALK_DOWNLOAD_URL="https://github.com/numberly/beanstalkd/archive/master.zip" \
	&& set -x \
	&& addgroup beanstalk \
	&& adduser -H -D -s /bin/false -G beanstalk beanstalk \
	&& apk add --update $buildDeps \
	&& curl -sSL "$BEANSTALK_DOWNLOAD_URL" -o /tmp/beanstalk.zip \
	&& mkdir -p /root/beanstalk \
	&& unzip /tmp/beanstalk.zip -d /root/beanstalk  \
	&& rm -f /tmp/beanstalk.zip \
	&& cd /root/beanstalk/beanstalkd-master \
	&& patch -p0 < /alpine.patch \
	&& make \
	&& cd \
	&& cp /root/beanstalk/beanstalkd-master/beanstalkd /bin/beanstalkd \
	&& rm -rf /alpine.patch /root/beanstalk \
	&& apk del $buildDeps \
	&& rm -rf  /var/cache/apk/* \
	;

EXPOSE 11300
CMD ["/bin/beanstalkd", "-F" , "-p", "11300"]