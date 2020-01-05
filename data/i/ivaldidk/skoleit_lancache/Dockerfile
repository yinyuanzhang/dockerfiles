FROM alpine

RUN apk add --no-cache nginx sniproxy unbound gawk runit; \
    rm /etc/nginx/conf.d/*; \
    touch /etc/unbound/unbound-lancache.conf

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/proxy.d/* /etc/nginx/proxy.d/
COPY nginx/conf.d/* /etc/nginx/conf.d/

COPY unbound/unbound.conf /etc/unbound/unbound.conf
COPY sniproxy/sniproxy.conf /etc/sniproxy/sniproxy.conf

COPY services /etc/sv
RUN chmod 755 /etc/sv/nginx/run; \
    chmod 755 /etc/sv/unbound/run; \
    chmod 755 /etc/sv/sniproxy/run; \
    chmod 755 /etc/sv/stats/run

COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh 

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "runsvdir", "-P /etc/sv" ]
