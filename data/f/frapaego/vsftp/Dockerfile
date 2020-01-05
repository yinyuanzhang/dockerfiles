FROM ubuntu:trusty

RUN apt-get update \
    && apt-get install -y --no-install-recommends vsftpd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/vsftpd/empty \
 && mkdir -p /etc/vsftpd \
 && mkdir -p /var/ftp \
 && mv /etc/vsftpd.conf /etc/vsftpd.orig

COPY init /

RUN chmod +x /init

ENV ANON_ROOT /var/ftp
ENV MAX_PER_IP 2
ENV MAX_LOGIN_FAILS 2
ENV MAX_CLIENTS 50
ENV MAX_RATE 6250000
ENV PASV_ADDRESS 127.0.0.1
ENV FTPD_BANNER "Welcome to an awesome public FTP Server"

VOLUME ["/var/ftp"]

EXPOSE 20-21
EXPOSE 65500-65515

ENTRYPOINT ["/init"]
