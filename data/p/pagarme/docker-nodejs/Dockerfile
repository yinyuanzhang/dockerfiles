FROM node:8.11-alpine as base

LABEL maintainer="pagarme"

ENV CREDSTASH_VERSION=v0.3.3

RUN apk update && apk add wget ca-certificates
#install gcredstash
RUN mkdir -p /opt/bin && \
    wget -O - https://github.com/winebarrel/gcredstash/releases/download/$CREDSTASH_VERSION/gcredstash-$CREDSTASH_VERSION-linux-amd64.gz | gunzip -c  > /opt/bin/gcredstash && \
    chmod a+x /opt/bin/gcredstash


FROM node:8.11-alpine as production

#region of the service
ENV AWS_REGION="us-east-1"

#type of environment (sandbox|live)
ENV APP_ENV="sandbox"

RUN apk --no-cache add ca-certificates

WORKDIR /root/

COPY --from=base /opt/bin/gcredstash /opt/bin/gcredstash

ADD entrypoint.sh /

RUN chmod a+x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
