# *************************************
#
# OMO AMS
#
# *************************************

FROM alpine:3.8

MAINTAINER XTech Cloud "xtech.cloud"

ENV container docker
ENV GIN_MODE release
ENV AMS_HTTP_ADDR :80
ENV AMS_ISS ams
ENV AMS_SECRET ams-secret
ENV AMS_HTTP_ADDR :80
ENV AMS_DATABASE_DRIVER sqlite
ENV AMS_SQLITE_FILEPATH /var/data/omo/omo.db
ENV AMS_MYSQL_ADDR 127.0.0.1:3306
ENV AMS_MYSQL_USER root
ENV AMS_MYSQL_PASSWORD mysql@OMO
ENV AMS_MYSQL_DATABASE omo
ENV AMS_LOG_FILE /var/log/omo/ams.log
ENV AMS_LOG_LEVEL INFO

VOLUME /var/data/omo
VOLUME /var/log/omo

EXPOSE 80

ADD ams /usr/local/bin/
RUN chmod +x /usr/local/bin/ams

CMD ["ams"]
