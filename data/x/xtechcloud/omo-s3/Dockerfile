# ************************************** 
#
# OMO VPN
#
# VERSION: 1.0.0
#
# *************************************

FROM alpine:3.8

MAINTAINER Easlee Liu "liu@easlee.me"

ENV container docker

ADD caddy /root/
ADD Caddyfile /root/

RUN chmod +x /root/caddy
RUN mkdir -p /root/upload/files

EXPOSE 7070
EXPOSE 7777
EXPOSE 7080

CMD ["/root/caddy", "-conf", "/root/Caddyfile"]
