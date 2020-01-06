FROM golang:1.10-alpine

ENV GHR_VERSION="0.10.2"

RUN apk add --update --no-cache git \
    && apk add --no-cache --virtual build-deps curl \
    && curl -fSL -o ghr.tar.gz "https://github.com/tcnksm/ghr/releases/download/v${GHR_VERSION}/ghr_v${GHR_VERSION}_linux_amd64.tar.gz" \
    && tar -xvzf ghr.tar.gz \
    && mv ghr_v${GHR_VERSION}_linux_amd64/ghr /usr/local/bin \
    && chown root:root /usr/local/bin/ghr \
    && rm -fr ghr.tar.gz ghr_v${GHR_VERSION}_linux_amd64 \
    && apk del --purge build-deps

ENTRYPOINT ["ghr"]
CMD ["--help"]
