FROM debian:buster-slim

ENV AUTHINFO="" \
    AUTO_UMOUNT=""

RUN apt-get update && apt-get install -y \
s3ql \
procps \
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

COPY ./docker/root /root
COPY ./docker/usr /usr

RUN chmod -R 600 /root/.s3ql

WORKDIR /root
ENTRYPOINT ["/usr/local/bin/init.sh"]
CMD ["/bin/bash"]
