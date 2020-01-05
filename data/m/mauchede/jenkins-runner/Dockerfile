FROM openjdk:jre-alpine

LABEL \
    maintainer="Morgan AUCHEDE <morgan.auchede@gmail.com>"

RUN set -e -u -x \
\
    # Install packages
\
    && apk add --no-cache --no-progress bash ca-certificates curl jq git openssh-client shadow \
\
    # Create user "jenkins"
\
    && groupadd --gid 1000 jenkins \
    && useradd --comment Jenkins --create-home --gid 1000 --home-dir /home/jenkins --shell /bin/sh --uid 1000 jenkins \
\
    # Clean
\
    && rm -f -r  /tmp/*
