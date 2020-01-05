# Node.js & Rails 4 environment
#
# VERSION               0.1

FROM glesage/nodejs-rails4
MAINTAINER Geoffroy Lesage

# SqLite
RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install sqlite libsqlite3-dev

# Decouple webapp from container
VOLUME ["/webapp"]

EXPOSE 3000

ADD start.sh /start.sh
RUN chmod +x /start.sh
ENTRYPOINT ["/start.sh"]