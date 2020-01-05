FROM openjdk:8-jre-alpine

ENV JAVA_OPTS "-Xmx1G"
ENV WATERFALL_ARGS ""
ENV UID=1000
ENV GID=1000
ENV WATERFALL_HOME=/data
ENV MEMORY=512m

EXPOSE 25565

VOLUME "${WATERFALL_HOME}"
WORKDIR ${WATERFALL_HOME}

RUN apk --no-cache add curl bash sudo

ADD https://ci.destroystokyo.com/job/Waterfall/lastSuccessfulBuild/artifact/Waterfall-Proxy/bootstrap/target/Waterfall.jar .

ADD start.sh /usr/bin/
RUN chmod +x /usr/bin/start.sh

RUN set -x \
	&& addgroup -g 1000 -S mcproxy \
	&& adduser -u 1000 -D -S -G mcproxy mcproxy \
	&& addgroup mcproxy wheel

CMD ["/usr/bin/start.sh"]
