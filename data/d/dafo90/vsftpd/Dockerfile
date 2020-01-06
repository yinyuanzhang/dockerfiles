FROM lsiobase/alpine:3.9

LABEL description="vsftpd Docker image based on Alpine Linux (lsiobase/alpine). Supports passive mode and virtual users." \
    license="Apache License 2.0" \
    usage="docker run -d -p [HOST PORT NUMBER]:21 -v [HOST FTP HOME]:/home/vsftpd dafo90/vsftpd" \
    version="1.0" \
    maintainer="dafo90"

# environment settings
ENV FTP_USER **String**
ENV FTP_PASS **Random**
ENV PASV_ADDRESS **IPv4**
ENV PASV_ADDR_RESOLVE NO
ENV PASV_ENABLE YES
ENV PASV_MIN_PORT 21100
ENV PASV_MAX_PORT 21110
ENV XFERLOG_STD_FORMAT NO
ENV LOG_STDOUT **Boolean**
ENV FILE_OPEN_MODE 0666
ENV LOCAL_UMASK 077
ENV PUID 1000
ENV PGID 1000

RUN \
    echo "**** install build packages ****" && \
    apk add --no-cache --virtual=build-dependencies --upgrade \
    build-base \
    linux-pam-dev \
    curl \
    tar && \
    echo "**** install runtime packages ****" && \
    apk add --no-cache --upgrade \
    vsftpd && \
    echo "**** compile libpam ****" && \
    mkdir /tmp/pam && \
    cd /tmp/pam && \
    curl -sSL https://github.com/prapdm/libpam-pwdfile/archive/v1.0.tar.gz | tar xz --strip 1 && \
    make install && \
    cd / && \
    echo "**** cleanup ****" && \
    apk del --purge \
    build-dependencies && \
    rm -rf \
    /tmp/* \
    /var/cache/apk/* \
    /var/log/* \
    /src

# copy local files
COPY root/ /

RUN \
    chmod +x \
    /usr/sbin/run-vsftpd.sh

# ports and volumes
EXPOSE 20 21
VOLUME /home/vsftpd
VOLUME /var/log/vsftpd

CMD ["/usr/sbin/run-vsftpd.sh"]