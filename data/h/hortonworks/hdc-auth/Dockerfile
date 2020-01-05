FROM hortonworks/hwx_node:10.4.1-alpine
MAINTAINER info@hortonworks.com

ENV SL_SERVER_PORT 3001
RUN apk add --no-cache curl bash git
EXPOSE 3001
ADD . /hortonworks-cloud-auth
RUN cd /hortonworks-cloud-auth && npm install
RUN cp -R /hortonworks-cloud-auth/schema /

CMD ["/hortonworks-cloud-auth/start-docker.sh"]
