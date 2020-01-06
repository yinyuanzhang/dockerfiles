FROM alpine:3.7

RUN apk add --no-cache python3 git && \
    pip3 install --upgrade pip setuptools httpie && \
    rm -r /root/.cache

ENTRYPOINT [ "http" ]
CMD ["--help"]
