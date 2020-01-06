FROM alpine:latest
MAINTAINER ZzenlD

RUN apk add --no-cache clamav-scanner clamav-libunrar rsync curl wget gnupg git tini bash bind-tools jq && \
    mkdir -p data var/lib/clamav-unofficial-sigs usr/local/bin etc/clamav-unofficial-sigs var/cache/vt-check && \
    git clone https://github.com/extremeshok/clamav-unofficial-sigs/ /tmp/clamav-unofficial-sigs/ && \
    cp /tmp/clamav-unofficial-sigs/clamav-unofficial-sigs.sh /usr/local/bin/clamav-unofficial-sigs.sh && \
    cp /tmp/clamav-unofficial-sigs/config/*.* /etc/clamav-unofficial-sigs/

COPY freshclam.conf /etc/clamav/freshclam.conf
COPY os.conf /etc/clamav-unofficial-sigs/os.conf
COPY user.conf /etc/clamav-unofficial-sigs/user.conf
COPY vt-check.sh /vt-check.sh
COPY run.sh /run.sh

RUN chmod 755 /usr/local/bin/clamav-unofficial-sigs.sh && \
    rm -rf /tmp/clamav-unofficial-sigs

ENV ANTIVIRUS_UPDATE_INTERVAL=900 \
    ANTIVIRUS_SCAN_INTERVAL=3600

CMD /run.sh
