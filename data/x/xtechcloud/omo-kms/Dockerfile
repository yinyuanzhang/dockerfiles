# ************************************** 
#
# OMO KMS
#
# VERSION: 1.0.0
#
# *************************************

FROM alpine:3.8

MAINTAINER XTech Cloud "xtech.cloud"

ENV container docker
ENV GIN_MODE release
ENV KMS_HTTP_ADDR :80
ENV KMS_GRPC_ADDR :10080
ENV KMS_DATABASE_DRIVER sqlite
ENV KMS_SQLITE_FILEPATH /etc/kms/kms.db
ENV KMS_MYSQL_ADDR 127.0.0.1:3306
ENV KMS_MYSQL_USER root
ENV KMS_MYSQL_PASSWORD mysql@OMO
ENV KMS_MYSQL_DATABASE kms

ADD kms /usr/local/bin/
RUN chmod +x /usr/local/bin/kms
RUN mkdir /etc/kms/

EXPOSE 80
EXPOSE 10080

CMD ["kms"]
