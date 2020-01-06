FROM alpine:latest
RUN apk add --update \
    py-pip \
   && pip install httpony
VOLUME ["/tmp"]
CMD httpony -l 0.0.0.0 -p 81 >> /tmp/index.html
EXPOSE 81
