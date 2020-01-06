FROM        alpine:3.8

LABEL       maintainer="SlothDS" \
            maintainer.mail="sloth@devils.su" \
            maintainer.git="https://github.com/slothds"

RUN         apk update && apk upgrade --no-cache && \
            apk add --no-cache bash shadow tzdata supervisor && \
            rm -rf /var/cache/apk/*
RUN         mkdir -p /opt /exec/env.d /exec/init.d && \
            crontab -u root -r && \
            groupadd -g 10001 runner && \
            useradd -u 10001 -g 10001 -G users -md /opt/runner -s /bin/false runner && \
            chown -R runner:runner /exec && chmod -R 775 /exec

COPY        rootfs /

ENTRYPOINT  ["/init"]

STOPSIGNAL  SIGTERM
