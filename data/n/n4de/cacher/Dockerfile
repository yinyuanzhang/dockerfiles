ARG ALPINE_VERSION=latest
FROM alpine:${ALPINE_VERSION} AS build

ENV VMTOUCH_VERSION=v1.3.1

WORKDIR /tmp

RUN apk add -U git make gcc musl-dev

RUN git clone https://github.com/hoytech/vmtouch.git && \
    cd vmtouch && \
    git checkout tags/${VMTOUCH_VERSION} && \
    make vmtouch


FROM alpine:${ALPINE_VERSION}

COPY --from=build /tmp/vmtouch/vmtouch /usr/local/bin/vmtouch

VOLUME [ "/data" ]
ENTRYPOINT [ "/usr/local/bin/vmtouch" ]
CMD ["-v", "-t", "/data"]