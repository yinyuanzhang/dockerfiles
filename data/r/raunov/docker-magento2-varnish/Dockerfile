FROM alpine
RUN apk update && \
apk upgrade && \
apk add varnish && \
apk add bind-tools

ENV VARNISH_PORT 80
ENV VARNISH_BACKEND 80
ENV BACKEND_HOST magento2

EXPOSE ${VARNISH_PORT}

COPY default.vcl /etc/varnish
ADD start /
ADD backendgen.sh /
RUN chmod +x /start /backendgen.sh
CMD ["/bin/sh","/start"]
