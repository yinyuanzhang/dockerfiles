FROM alpine:3.3

# Update packages and certs, install bash, clear apk cache
RUN \
    apk update && \
    apk upgrade && \
    apk add ca-certificates && \
    update-ca-certificates && \
    apk add --update bash && \
    rm -rf /var/cache/apk/*

# Install Dockerize
ENV DOCKERIZE_VERSION v0.2.0
RUN \
    wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
    tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
    rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Create our app directory
RUN mkdir /app