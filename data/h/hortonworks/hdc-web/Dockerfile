FROM hortonworks/hwx_node:10.4.1-alpine
MAINTAINER info@hortonworks.com

ENV ULU_SERVER_PORT 3000
RUN apk add --no-cache curl bash git
EXPOSE 3000
ADD . /hortonworks-cloud-web
RUN ./hortonworks-cloud-web/build-n-clean.sh

CMD ["/hortonworks-cloud-web/start-docker.sh"]
