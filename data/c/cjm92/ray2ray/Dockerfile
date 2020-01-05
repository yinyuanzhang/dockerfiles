FROM ubuntu:latest as builder

RUN apt-get update
RUN apt-get install curl -y
RUN curl -L -o /tmp/go.sh https://install.direct/go.sh
RUN chmod +x /tmp/go.sh
RUN /tmp/go.sh

FROM alpine:latest

LABEL maintainer "ray2ray <admin@ray2ray.com>"
ENV CONFIG=https://pastebin.com/raw/hBr3fDw9

COPY --from=builder /usr/bin/v2ray/v2ray /usr/bin/ray2ray/
COPY --from=builder /usr/bin/v2ray/v2ctl /usr/bin/ray2ray/
COPY --from=builder /usr/bin/v2ray/geoip.dat /usr/bin/ray2ray/
COPY --from=builder /usr/bin/v2ray/geosite.dat /usr/bin/ray2ray/

RUN set -ex && \
    apk --no-cache add ca-certificates && \
    mv -f /usr/bin/ray2ray/v2ray /usr/bin/ray2ray/ray2ray &&\
    chmod +x /usr/bin/ray2ray/*

ENV PATH /usr/bin/ray2ray:$PATH

CMD exec ray2ray\
	-config=$CONFIG
