FROM alpine
ENV PASSWORD= \
    ARGS=
RUN apk add --no-cache aria2 \
    && mkdir -p /root/.aria2/session \
    && touch /root/.aria2/session/aria2.session
VOLUME /data
COPY aria2.conf /root/.aria2/aria2.conf
CMD exec aria2c \
    --rpc-secret=${PASSWORD:-$(hostname)} \
    $ARGS
