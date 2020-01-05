FROM alpine:3.5

RUN set -x \
 && apk add --update --no-cache \
        ca-certificates \
        duplicity \
        openssh \
        openssl \
        py-crypto \
        py-pip \
        py-paramiko \
        py-setuptools \
        rsync \
        mysql-client \
        gawk \
        postgresql \
 && update-ca-certificates \
 && pip install pydrive==1.3.1 \
 && apk del --purge py-pip \
 && rm -rf /var/cache/apk/*
 
COPY entrypoint.awk /entrypoint.awk
RUN chmod +x /entrypoint.awk
 
VOLUME ["/root/.cache/duplicity", "/root/.gnupg"]
 
CMD ["/entrypoint.awk", "/backupmanager.conf"]