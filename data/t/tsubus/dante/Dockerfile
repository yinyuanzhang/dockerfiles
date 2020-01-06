FROM tsubus/alpine

RUN set -x \
    # add testing repo
 && echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
 && apk upgrade --no-cache \
    # Runtime dependencies.
 && apk add --no-cache \
        linux-pam \
        dante-server@testing \
     # Clean up.
 && rm -rf /tmp/*

# add local files
COPY root/ /

# expose /config
VOLUME /config
