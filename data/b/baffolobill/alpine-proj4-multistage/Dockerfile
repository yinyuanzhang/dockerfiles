FROM alpine:3.8

# Django v2.1.x supported versions table
# https://docs.djangoproject.com/en/2.1/ref/contrib/gis/install/geolibs/

# PROJ.4 v4.9
ARG PROJ4_URL="https://git.alpinelinux.org/aports/plain/testing/proj4/APKBUILD?id=4229ea8e8fa049f529b3d09996d7e21cd4718ee9"


# Details here:
# https://superuser.com/a/1351074

RUN \
    apk -U add alpine-sdk && \
    adduser -D packager && \
    addgroup packager abuild

USER packager

RUN \
    cd /tmp && \
    wget -O APKBUILD "${PROJ4_URL}" && \
    abuild-keygen -a -i && \
    abuild -r
