# *************************************
#
# OMO APP
#
# *************************************

FROM alpine:3.8

MAINTAINER XTech Cloud "xtech.cloud"

ENV container docker
ENV GIN_MODE release
ENV APP_HTTP_ADDR :80
ENV APP_DATABASE_DRIVER sqlite
ENV APP_SQLITE_FILEPATH /var/data/omo/omo.db
ENV APP_MYSQL_ADDR 127.0.0.1:3306
ENV APP_MYSQL_USER root
ENV APP_MYSQL_PASSWORD mysql@OMO
ENV APP_MYSQL_DATABASE omo
ENV APP_LOG_FILE /var/log/omo/app.log
ENV APP_LOG_LEVEL INFO

VOLUME /var/data/omo
VOLUME /var/log/omo

EXPOSE 80

ADD app /usr/local/bin/
RUN chmod +x /usr/local/bin/app

CMD ["app"]
