FROM alpine:latest
WORKDIR /opt
RUN apk update && \
    apk upgrade && \
    apk add curl tar
RUN curl -LO  https://github.com/ronggang/transmission-web-control/archive/v1.5.1.tar.gz && tar -xf v1.5.1.tar.gz



FROM alpine:latest
MAINTAINER Ludovic Logiou <ludovic.logiou@gmail.com>
RUN apk update && \ 
    apk upgrade && \
    apk add transmission-daemon
COPY --from=0 /opt/transmission-web-control-1.5.1/* /usr/share/transmission/web/
ADD settings.json /etc/transmission-daemon/settings.json
EXPOSE 9091
COPY entrypoint.sh /usr/bin/
ENTRYPOINT ["/usr/bin/entrypoint.sh"]
