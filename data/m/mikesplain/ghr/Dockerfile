FROM alpine:3.7

ENV GHR_VERSION="0.9.0"

RUN apk add --no-cache \
        git && \
    apk add --no-cache --virtual build-dependencies \
        curl \
        tar && \
    curl -fSL -o ghr.tar.gz "https://github.com/tcnksm/ghr/releases/download/v${GHR_VERSION}/ghr_v${GHR_VERSION}_linux_amd64.tar.gz" && \
    mkdir -p /tmp/ghr && \
    tar -zxvf ghr.tar.gz -C /tmp/ghr --strip-components=1 && \
    mv /tmp/ghr/ghr /usr/local/bin/ghr && \
    rm -rf ghr.tar.gz /tmp/ghr && \
    apk del --purge build-dependencies

ENTRYPOINT ["ghr"]
CMD ["--help"]
