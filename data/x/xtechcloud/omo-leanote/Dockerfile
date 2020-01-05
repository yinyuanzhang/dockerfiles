# ************************************** #
# OMO Moonote
#
# VERSION: 1.0.0
#
# *************************************

FROM alpine:3.6

MAINTAINER Easlee Liu "easlee@outlook.com"

ENV container docker

VOLUME /omo

###############################
# install applications
###############################
RUN apk add --no-cache bash
RUN apk add --no-cache mongodb
RUN apk add --no-cache mongodb-tools

RUN echo mkdir -p /omo/log/mongodb > /root/init_path.sh
RUN echo mkdir -p /omo/data/mongodb >> /root/init_path.sh
RUN echo mongorestore -h localhost -d leanote --dir /root/leanote/mongodb_backup/leanote_install_data/ > /root/init_mongo.sh
RUN chmod +x /root/init_path.sh
RUN chmod +x /root/init_mongo.sh

ADD dep/entry.sh /usr/local/bin/
ADD dep/mongod.conf /etc/
ADD dep/leanote-linux-amd64-v2.6.1.bin.tar.gz /root/

EXPOSE 9000

CMD ["entry.sh"]
