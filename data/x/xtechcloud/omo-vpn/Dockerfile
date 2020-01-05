# ************************************** 
#
# OMO VPN
#
# VERSION: 1.0.0
#
# *************************************

FROM alpine:3.7

MAINTAINER Easlee Liu "liu@easlee.me"

ENV container docker

ADD shadowsocks.cfg /config.json
ADD shadowsocks-server /usr/bin/

EXPOSE 3301

CMD ["shadowsocks-server"]
