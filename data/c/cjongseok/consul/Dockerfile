# The original image is progrium/consul by Jeff Lindsay <progrium@gmail.com>
#

FROM alpine:3.2
RUN apk --update add curl bash ca-certificates jq && \
    curl -Ls https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-2.21-r2.apk > /tmp/glibc-2.21-r2.apk && \
    apk add --allow-untrusted /tmp/glibc-2.21-r2.apk && \
    rm -rf /tmp/glibc-2.21-r2.apk /var/cache/apk/*

#ADD https://dl.bintray.com/mitchellh/consul/0.5.2_linux_amd64.zip /tmp/consul.zip
ADD https://releases.hashicorp.com/consul/0.6.3/consul_0.6.3_linux_amd64.zip /tmp/consul.zip
RUN cd /bin && unzip /tmp/consul.zip && chmod +x /bin/consul && rm /tmp/consul.zip

#ADD https://dl.bintray.com/mitchellh/consul/0.5.2_web_ui.zip /tmp/webui.zip
ADD https://releases.hashicorp.com/consul/0.6.3/consul_0.6.3_web_ui.zip /tmp/webui.zip
#RUN mkdir /ui && cd /ui && unzip /tmp/webui.zip && rm /tmp/webui.zip && mv dist/* . && rm -rf dist
RUN mkdir /ui && cd /ui && unzip /tmp/webui.zip && rm /tmp/webui.zip

ADD https://get.docker.io/builds/Linux/x86_64/docker-1.6.1 /bin/docker
RUN chmod +x /bin/docker

# RUN opkg-install curl bash ca-certificates

# RUN cat /etc/ssl/certs/*.crt > /etc/ssl/certs/ca-certificates.crt && \
#    sed -i -r '/^#.+/d' /etc/ssl/certs/ca-certificates.crt

ADD ./config /config/
#ONBUILD ADD ./config /config/

ADD ./start /bin/start
#ADD ./check-http /bin/check-http
#ADD ./check-cmd /bin/check-cmd

EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 53 53/udp
VOLUME ["/data"]

ENV SHELL /bin/bash

ENTRYPOINT ["/bin/start"]
#CMD []
