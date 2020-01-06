FROM ubuntu:14.04

RUN echo "America/Argentina/Buenos_Aires" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

RUN apt-get update && \
    apt-get install -y memcached && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 11211

CMD ["memcached", "-u", "daemon"]
