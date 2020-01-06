FROM alpine:3.7

ENV REFRESHED_AT=2018-07-19 \
    LANG=en_US.UTF-8 \
    HOME=/opt/app \
    TERM=xterm

RUN \
    #Install Dependencies for Erlang and Distillery \
    apk add --no-cache \
        ncurses-libs \
        zlib \
        openssl \
        ca-certificates \
        bash && \
    update-ca-certificates --fresh && \
    #Install bash which is required by Distillery \
    #Create /opt/app directory and default user \
    mkdir -p ${HOME} && \
    adduser -s /bin/sh -u 1001 -G root -h ${HOME} -S -D default && \
    chown -R 1001:0 ${HOME} && \
    apk --no-cache upgrade

WORKDIR ${HOME}
CMD ["/bin/bash"]
