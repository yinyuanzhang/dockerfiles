FROM alpine:edge
LABEL maintainer='sedunne@icanhazmail.net'

ENV VERS 3.6-r0

RUN apk add --no-cache --update bitlbee=$VERS bitlbee-otr=$VERS
RUN /usr/sbin/adduser -h /var/lib/bitlbee -s /sbin/nologin -DH bitlbee &&\
    chown -R bitlbee:bitlbee /var/lib/bitlbee && \
    touch /var/run/bitlbee.pid && chown bitlbee:bitlbee /var/run/bitlbee.pid

USER bitlbee
VOLUME ["/var/lib/bitlbee"]
EXPOSE 6667

ENTRYPOINT ["bitlbee"]
CMD ["-Fnv"]
