FROM dockercore/golang-cross:1.12.12

LABEL maintainer="cbroglie@gmail.com"

ENV GORELEASER_VERSION=0.120.4
ENV GORELEASER_SHA=31365246c21550fc13fc7b1f9f7f2301196ba1e623e459db98c58439c3a4e2b5

ENV GORELEASER_DOWNLOAD_FILE=goreleaser_Linux_x86_64.tar.gz
ENV GORELEASER_DOWNLOAD_URL=https://github.com/goreleaser/goreleaser/releases/download/v${GORELEASER_VERSION}/${GORELEASER_DOWNLOAD_FILE}

RUN wget ${GORELEASER_DOWNLOAD_URL}; \
    echo "$GORELEASER_SHA $GORELEASER_DOWNLOAD_FILE" | sha256sum -c - || exit 1; \
    tar -xzf $GORELEASER_DOWNLOAD_FILE -C /usr/bin/ goreleaser; \
    rm $GORELEASER_DOWNLOAD_FILE;

RUN apt-get update && \
    apt-get install -y --no-install-recommends musl-tools

CMD ["goreleaser", "-v"]
