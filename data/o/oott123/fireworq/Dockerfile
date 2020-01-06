FROM alpine:3.10

ENV FIREWORQ_QUEUE_DEFAULT default
ENV FIREWORQ_BIND 0.0.0.0:8080

RUN apk --no-cache add curl unzip jq \
 && mkdir -p /tmp/build \
 && curl -L $(curl -sL https://api.github.com/repos/fireworq/fireworq/releases/tags/v1.2.1 | jq -r '.assets[].browser_download_url' | grep "_linux_amd64.zip") -o /tmp/build/fireworq_linux_amd64.zip \
 && cd /usr/local/bin \
 && unzip /tmp/build/fireworq_linux_amd64.zip fireworq \
 && chmod a+x /usr/local/bin/fireworq \
 && rm -rf /tmp/build \
 && apk del --purge curl unzip \
 && fireworq --version

EXPOSE 8080

CMD ["fireworq"]
