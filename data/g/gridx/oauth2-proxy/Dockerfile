FROM alpine:3.6
RUN apk --no-cache add ca-certificates wget tar
WORKDIR /root/
RUN wget https://github.com/bitly/oauth2_proxy/releases/download/v2.2/oauth2_proxy-2.2.0.linux-amd64.go1.8.1.tar.gz && \
    tar xvzf oauth2_proxy-2.2.0.linux-amd64.go1.8.1.tar.gz && \
    mv oauth2_proxy-2.2.0.linux-amd64.go1.8.1/oauth2_proxy /usr/local/bin/oauth2_proxy
ENTRYPOINT ["/usr/local/bin/oauth2_proxy"]
