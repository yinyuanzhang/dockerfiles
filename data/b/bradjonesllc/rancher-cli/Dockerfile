FROM rancher/cli:v2.0.4

RUN apk add --no-cache curl

RUN mkdir -p /root/.rancher && touch /root/.rancher/cli2.json

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin

COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
