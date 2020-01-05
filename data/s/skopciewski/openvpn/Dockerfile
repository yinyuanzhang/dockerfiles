FROM alpine:3.9

RUN apk add --no-cache openvpn bash
COPY data/entrypoint /entrypoint
RUN chmod 755 /entrypoint

ENV OPENVPN_HOME /mnt/openvpn
WORKDIR ${OPENVPN_HOME}
EXPOSE 1194/udp

ENTRYPOINT ["/entrypoint"]
CMD ["--config", "server.conf"]
