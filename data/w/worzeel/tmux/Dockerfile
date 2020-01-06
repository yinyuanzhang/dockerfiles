FROM alpine

RUN echo http://nl.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories \
    && echo http://nl.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories \
    && apk update \
    && apk upgrade \
    && apk add shadow tmux bash ncurses \
    && rm -rf /var/cache/apk/* \
    && usermod -s /bin/bash root

COPY base/.tmux.conf /root/.tmux.conf
COPY base/.profile /root/.profile

CMD tmux
