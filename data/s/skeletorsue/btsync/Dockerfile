FROM debian:stretch
MAINTAINER Chris Staley me@unixtime.site

RUN apt-get update && apt-get install -y curl
RUN apt-get -y clean && rm -rf /var/lib/apt/lists/*

RUN curl -o /usr/bin/btsync.tar.gz https://download-cdn.resilio.com/stable/linux-x64/resilio-sync_x64.tar.gz
RUN cd /usr/bin && tar -xzvf btsync.tar.gz && rm btsync.tar.gz

VOLUME /btsync

EXPOSE 8888
EXPOSE 55555

ENTRYPOINT ["rslsync"]

# Default arguments:
CMD ["--storage", "/btsync", "--webui.listen", "0.0.0.0:8888", "--config", "/btsync/btsync.conf", "--nodaemon"]
