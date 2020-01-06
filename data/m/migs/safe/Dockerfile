FROM vault:latest

ENV SAFE_VERSION=1.1.0

RUN apk add ca-certificates

RUN wget https://github.com/starkandwayne/safe/releases/download/v${SAFE_VERSION}/safe-linux-amd64 && \
    mv safe-linux-amd64 /usr/local/bin/safe && \
    chmod +x /usr/local/bin/safe