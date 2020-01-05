FROM certbot/certbot:v0.37.2

ENV KUBECTL_VERSION="v1.15.0"

# Tools that may be useful in a post-hook script
RUN apk add --no-cache openssh rsync curl \
    && curl -LO https://storage.googleapis.com/kubernetes-release/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl \
    && chmod +x ./kubectl \
    && mv ./kubectl /usr/local/bin/kubectl

COPY run.sh /run.sh
COPY cert-gen.sh /usr/bin/cert-gen

ENV CRON_SCHEDULE="0 10 * * MON" \
    CRON_COMMAND="certbot renew"

VOLUME ["/etc/letsencrypt", "/var/log/letsencrypt", "/certificates"]

ENTRYPOINT ["/run.sh"]
