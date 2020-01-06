FROM alpine
RUN apk add --no-cache runit bitcoin

COPY entrypoint.sh /entrypoint.sh

# keychain / wallet directory
VOLUME /var/lib/bitcoin

# core service port
EXPOSE 8333

# json RPC
EXPOSE 8332

CMD ["/entrypoint.sh"]
