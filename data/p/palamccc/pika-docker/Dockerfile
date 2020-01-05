FROM debian:stretch-slim
RUN cd /tmp \
  && apt-get update \
  && apt-get install -y --no-install-recommends wget ca-certificates bzip2 \
  && wget https://github.com/Qihoo360/pika/releases/download/v2.3.5/pika-linux-x86_64-v2.3.5.tar.bz2 \
  && tar xjvf /tmp/pika-linux*.tar.bz2 \
  && mkdir /pika \
  && mv output/* /pika \
  && apt-get remove -y wget ca-certificates bzip2 \
  && apt-get autoremove -y \
  && rm -rf /tmp /var/lib/apt/lists/*
EXPOSE 9221
CMD ["/pika/bin/pika", "-c", "/pika/conf/pika.conf"]