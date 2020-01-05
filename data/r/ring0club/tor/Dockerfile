FROM alpine:3.10.1
RUN apk upgrade \
    --repository https://nl.alpinelinux.org/alpine/edge/main \
    --no-cache
RUN apk add tor=0.4.0.5-r0 \
    --repository http://nl.alpinelinux.org/alpine/edge/community \
    --no-cache
#VOLUME /etc/tor
USER tor
ENTRYPOINT ["tor"]
