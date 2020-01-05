FROM alpine:3.8

RUN apk add --no-cache apcupsd openssh-client sshpass msmtp mailx wget

COPY mail.rc /etc/mail.rc
COPY config /etc/apcupsd/config
COPY apcupsd.conf /etc/apcupsd/apcupsd.conf

COPY msmtp-wrapper /usr/bin/msmtp-wrapper
RUN chmod +x /usr/bin/msmtp-wrapper

COPY hostname /usr/local/bin/hostname
RUN chmod +x /usr/local/bin/hostname

COPY doshutdown /etc/apcupsd/doshutdown
RUN chmod +x /etc/apcupsd/doshutdown

CMD apcupsd -b
