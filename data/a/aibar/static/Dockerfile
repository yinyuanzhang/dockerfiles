FROM aibar/alpine

VOLUME /data

EXPOSE 8000

WORKDIR /data

ENTRYPOINT ["python", "-m", "SimpleHTTPServer", "8000"]

RUN apk update && \
    apk add python && \
    rm -rf /var/cache/apk/*
