FROM alpine
RUN sed -i -e 's/v[[:digit:]]\.[[:digit:]]+/edge/g' /etc/apk/repositories && \
    apk update && \
    apk add newsboat && \
    rm -rf /var/cache/apk/*
ENTRYPOINT ["newsboat"]
