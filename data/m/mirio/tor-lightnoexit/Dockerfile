FROM alpine:3.8

RUN apk add --no-cache tor && echo -ne "ExitRelay 0\nSOCKSPort 0.0.0.0:9050\nControlPort 0.0.0.0:9051" > /etc/tor/torrc

EXPOSE 9050 9051
USER tor

CMD ["/usr/bin/tor"]
