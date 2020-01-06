FROM alpine:3.10
RUN \
    apk add --no-progress --no-cache dnscache tini \
    && echo 127.0.0.11 > /etc/dnscache/servers/@ \
    && touch /etc/dnscache/ip/172
ADD entrypoint.sh /entrypoint.sh
EXPOSE 53
ENTRYPOINT [ "/sbin/tini", "--" ]
CMD [ "/entrypoint.sh" ]
