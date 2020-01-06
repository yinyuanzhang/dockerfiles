FROM phusion/baseimage:0.11

ENV SEAFILE_VERSION=6.3.4 SEAFILE_SERVER=seafile-server

RUN mkdir -p /opt/seafile/ && \
    curl -sSL -o - https://download.seadrive.org/seafile-server_${SEAFILE_VERSION}_x86-64.tar.gz \
    | tar xzf - -C /opt/seafile/

COPY init.sh /init.sh
COPY seafile.sh /seafile.sh
COPY nginx.conf /nginx.conf

RUN /bin/bash /init.sh

RUN rm -rf \
    /root/.cache \
    /root/.npm \
    /root/.pip \
    /usr/local/share/doc \
    /usr/share/doc \
    /usr/share/man \
    /usr/share/vim/vim74/doc \
    /usr/share/vim/vim74/lang \
    /usr/share/vim/vim74/spell/en* \
    /usr/share/vim/vim74/tutor \
    /var/lib/apt/lists/* \
    /tmp/*

EXPOSE 80
VOLUME ["/opt/seafile"]

CMD ["/server.sh", "restart"]
