FROM alpine:3.4
LABEL maintainer "Synchro Food <developer@synchro-food.co.jp>"

COPY cacher.sh wait_for_lock.sh /usr/local/
RUN mkdir /cache && apk add --no-cache bash rsync findutils && \
    chmod 755 /usr/local/cacher.sh && \
    chmod 755 /usr/local/wait_for_lock.sh
VOLUME /cache

ENTRYPOINT ["/usr/local/cacher.sh"]
