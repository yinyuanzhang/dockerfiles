FROM augustash/alpine-phpfpm:4.0.0

# packages & configure
RUN apk-install php7-dev@php php7-xdebug@php sudo && \
    apk-cleanup

# copy root filesystem
COPY rootfs /

# external
EXPOSE 9000 9004
WORKDIR /src

# run s6 supervisor
ENTRYPOINT ["/init"]
