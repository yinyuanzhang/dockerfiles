FROM telegraf:alpine

RUN apk add --no-cache --virtual .build-deps net-snmp net-snmp-tools

EXPOSE 8125/udp 8092/udp 8094

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
VOLUME "/etc/telegraf/mibs"
ENTRYPOINT ["/entrypoint.sh"]
CMD ["telegraf"]