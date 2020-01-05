FROM alpine:edge
ENV CONFIG_JSON=none
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
 && apk add --no-cache --virtual .build-deps ca-certificates curl bash \
 && curl https://install.direct/go.sh | bash \
 && rm -rf /usr/bin/v2ray/geoip.dat /usr/bin/v2ray/geosite.dat \
 && chgrp -R 0 /etc/v2ray \
 && chmod -R g+rwX /etc/v2ray
ADD configure.sh /configure.sh
RUN chmod +x /configure.sh
ENTRYPOINT /configure.sh
EXPOSE 80 8080
