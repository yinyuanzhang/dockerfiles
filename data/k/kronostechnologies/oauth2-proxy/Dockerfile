FROM debian:stretch-slim
RUN apt-get update && apt-get -qq -y install wget tar
RUN wget -qO- https://github.com/weargoggles/oauth2_proxy/releases/download/v2.2-websocket/oauth2_proxy-2.2.0.linux-amd64.go1.8.tar.gz | tar zxfO - > /usr/local/bin/oauth2_proxy && chmod +x /usr/local/bin/oauth2_proxy

