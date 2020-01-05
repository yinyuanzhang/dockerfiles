FROM alpine:3.5

RUN apk --no-cache add bash gzip groff less python py-pip tar openssl ca-certificates gnupg && \
    pip --no-cache-dir install awscli==1.11.76 && \
    apk --purge -v del py-pip

COPY backup.sh /usr/bin/backup.sh
COPY gpg.conf /root/.gnupg/gpg.conf
COPY dirmngr.conf /root/.gnupg/dirmngr.conf

RUN chmod 0600 /root/.gnupg

CMD /usr/bin/backup.sh
