FROM ubuntu:latest as builder

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install curl -y
RUN curl -L -o /tmp/go.sh https://install.direct/go.sh
RUN chmod +x /tmp/go.sh
RUN /tmp/go.sh

FROM alpine:latest

LABEL maintainer "Darian Raymond <admin@v2ray.com>"

COPY --from=builder /usr/bin/v2ray/v2ray /usr/bin/v2ray/
COPY --from=builder /usr/bin/v2ray/v2ctl /usr/bin/v2ray/
COPY --from=builder /usr/bin/v2ray/geoip.dat /usr/bin/v2ray/
COPY --from=builder /usr/bin/v2ray/geosite.dat /usr/bin/v2ray/

COPY config.json /etc/v2ray/config.json

RUN set -ex && \
    apk --no-cache add ca-certificates && \
#    mkdir /var/log/v2ray/ &&\
    chmod +x /usr/bin/v2ray/v2ctl && \
    chmod +x /usr/bin/v2ray/v2ray

ENV PATH /usr/bin/v2ray:$PATH
USER v2ray
ENV USER=v2ray

EXPOSE 8080
EXPOSE 8081

CMD cp /etc/v2ray/config.json /tmp/config.json && \
    sed -i "s/b831381d-6324-4d53-ad4f-8cda48b30811/${ID}/g" /tmp/config.json && \
    sed -i "s/HTTPUSER/${USER}/g" /tmp/config.json && \
    sed -i "s/HTTPPASS/${PASS}/g" /tmp/config.json && \
    v2ray -config=/tmp/config.json
