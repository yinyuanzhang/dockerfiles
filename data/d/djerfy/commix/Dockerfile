FROM alpine:3.9
LABEL description="Commix docker container" \
      maintainer="Djerfy <djerfy@gmail.com>"

ENV VERSION=2.9-20190626

RUN apk -U add python wget && \
    wget https://github.com/commixproject/commix/archive/v${VERSION}.tar.gz -O commix.tar.gz && \
    tar xzf commix.tar.gz && \
    rm -f commix.tar.gz && \
    mv commix-${VERSION} /commix && \
    apk del wget

ENTRYPOINT ["/commix/commix.py"]

