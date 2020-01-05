FROM alpine:latest

LABEL maintainer="Romain THERRAT <romain@pockost.com>"

RUN apk add --no-cache git python \
 && crontab -l | { cat; echo "* * * * * sh /usr/local/bin/update-crs.sh"; } | crontab -

COPY update-crs.sh /usr/local/bin
COPY initial-crs.sh /usr/local/bin

ENTRYPOINT [ "/usr/local/bin/initial-crs.sh" ]

CMD [ "crond", "-f" ]
