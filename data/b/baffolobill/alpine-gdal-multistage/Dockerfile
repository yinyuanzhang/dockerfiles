FROM alpine:3.8

# GDAL v2.2.4
ARG GDAL_URL="https://git.alpinelinux.org/aports/plain/testing/gdal/APKBUILD?id=2d067bec953a86bb05587346f00631dfd5698ad5"

RUN \
    apk -U add alpine-sdk && \
    adduser -D packager && \
    addgroup packager abuild

USER packager

RUN \
    cd /tmp && \
    wget -O APKBUILD "${GDAL_URL}" && \
    abuild-keygen -a -i && \
    abuild -r
    
