FROM pandoc/latex

RUN apk update && apk add \
    bash \
    git

ENTRYPOINT ["/bin/bash", "-l", "-c"]

WORKDIR /build
