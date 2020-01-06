FROM alpine:3.8

RUN apk update
RUN apk add --no-cache squid acf-squid su-exec
RUN rm -rf /var/lib/apt/lists/*
RUN /usr/lib/squid/ssl_crtd -c -s /var/lib/ssl_db
#RUN squid -z

COPY ./squid.conf /etc/squid/squid.conf
COPY ./squid.pem /etc/squid/squid.pem
COPY ./hosts.txt /etc/squid/hosts.txt
COPY ./entrypoint.sh /sbin/entrypoint.sh

RUN chmod 755 /sbin/entrypoint.sh



ENTRYPOINT [ "/sbin/entrypoint.sh" ]
# CMD [ "squid" ]

EXPOSE 3128/tcp

#RUN squid -k reconfigure