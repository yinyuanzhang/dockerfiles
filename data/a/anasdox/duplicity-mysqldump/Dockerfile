FROM alpine:3.8

ENV HOME=/home/duplicity
WORKDIR /home/duplicity

ENV BUILD_DEPS="tzdata" \
    RUNTIME_DEPS="bash mysql-client ca-certificates duplicity lftp openssh openssl rsync shadow"

RUN set -x && \
    apk add --update $RUNTIME_DEPS && \
    apk add --virtual build_deps $BUILD_DEPS && \
    cp /usr/share/zoneinfo/Europe/Paris /etc/localtime && \
    apk del build_deps && \
    update-ca-certificates

RUN set -x && \
    adduser -D -u 1000 duplicity && \
    groupmod -g 82 duplicity && \
    mkdir -p /home/duplicity/.cache/duplicity && \
    mkdir -p /home/duplicity/.gnupg && \
    su - duplicity -c 'duplicity --version' && \
    chmod -R go+rwx /home/duplicity/ && \
    chmod -R 600 /home/duplicity/.gnupg && \
    chown -R duplicity:duplicity /home/duplicity/

ADD backup.sh /
ADD restore.sh /

RUN echo '@hourly /bin/su -c "/backup.sh" -s /bin/bash duplicity' > /etc/crontabs/root

CMD ["crond", "-f"]