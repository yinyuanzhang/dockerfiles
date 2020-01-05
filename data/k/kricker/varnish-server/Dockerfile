FROM alpine:latest
ENV VARNISH_BACKEND_ADDRESS 192.168.1.65
ENV VARNISH_MEMORY 900M
ENV VARNISH_PORT 8080
ENV VARNISH_BACKEND_PORT 80
EXPOSE 80
EXPOSE 8080

RUN apk update && \
    apk upgrade && \
    apk add varnish

ADD start.sh /start.sh
RUN chmod 777 /start.sh
CMD ["/start.sh"]
