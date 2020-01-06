# *************************************
#
# OMO VPP
#
# VERSION: 1.1.1
#
# *************************************

FROM alpine:3.8

MAINTAINER XTech Cloud "xtech.cloud"

ENV container docker
ENV GIN_MODE release
ENV VPP_HTTP_ADDR :80
ENV VPP_HTTPS_ADDR :443
ENV VPP_WS_ADDR :8000
ENV VPP_CONFIG /etc/vpp/vpp.yaml
ENV VPP_TLS_CRT /etc/vpp/tls.crt
ENV VPP_TLS_KEY /etc/vpp/tls.key

VOLUME /etc/vpp

EXPOSE 80
EXPOSE 443
EXPOSE 8000

ADD vpp /usr/local/bin/
RUN chmod +x /usr/local/bin/vpp
ADD vpp.yaml /etc/vpp/
ADD tls.crt /etc/vpp/
ADD tls.key /etc/vpp/

CMD ["vpp"]
