FROM alpine:3.8

# Django v2.1.x supported versions table
# https://docs.djangoproject.com/en/2.1/ref/contrib/gis/install/geolibs/

# GEOS v3.6.2
ARG GEOS_URL="https://git.alpinelinux.org/aports/plain/testing/geos/APKBUILD?id=d131db6d9d084e11911b6899b9429a17345706a2"

# Details here:
# https://superuser.com/a/1351074

RUN \
    apk -U add alpine-sdk && \
    adduser -D packager && \
    addgroup packager abuild

USER packager

RUN \
    cd /tmp && \
    wget -O APKBUILD "${GEOS_URL}" && \
    abuild-keygen -a -i && \
    abuild -r
