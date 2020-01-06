FROM debian
RUN apt-get update && apt-get -y upgrade && apt-get -y install parted udev && apt-get clean
COPY entrypoint.sh /
COPY pishrink.sh /usr/local/bin/
WORKDIR /workspace
ENTRYPOINT ["/entrypoint.sh"]
