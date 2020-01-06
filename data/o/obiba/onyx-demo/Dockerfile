#
# Onyx demo Dockerfile
#
# https://github.com/obiba/docker-onyx-demo
#

# Pull base image
FROM jetty:9-jre8

MAINTAINER OBiBa <dev@obiba.org>

ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

ENV ONYX_DEMO_WAR=1.12-SNAPSHOT/onyx-demo-1.12-20180629.162027-1.war

# Install Onyx demo
RUN \
  cd /tmp && \
  wget -q -O onyx-demo.war https://obiba.jfrog.io/obiba/libs-snapshot-local/org/obiba/onyx/onyx-demo/${ONYX_DEMO_WAR} && \
  mv onyx-demo.war /var/lib/jetty/webapps/root.war && \
  chown jetty:jetty /var/lib/jetty/webapps/root.war

# Define default command.
CMD ["jetty.sh", "run"]

# http
EXPOSE 8080
