# vim:set ft=dockerfile:
FROM debian:stretch-slim

LABEL maintainer="Andrius Kairiukstis <k@andrius.mobi>"

ENV ASTERISK_VERSION 16-current
ENV OPUS_CODEC       asterisk-16.0/x86-64/codec_opus-16.0_current-x86_64

COPY build-asterisk.sh /
RUN /build-asterisk.sh

COPY ssmtp.conf /etc/ssmtp/ssmtp.conf

EXPOSE 5060/udp 5060/tcp
VOLUME /etc/asterisk /usr/lib/asterisk /var/lib/asterisk /var/spool/asterisk /var/log/asterisk

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/sbin/asterisk", "-vvvdddf", "-T", "-W", "-U", "asterisk", "-p"]
