FROM alpine
ENV GOBGP_VERSION=2.7.0
ADD https://github.com/osrg/gobgp/releases/download/v${GOBGP_VERSION}/gobgp_${GOBGP_VERSION}_linux_amd64.tar.gz /
RUN tar zxvf /gobgp_${GOBGP_VERSION}_linux_amd64.tar.gz

FROM alpine
RUN apk add --no-cache bash
COPY --from=0 /gobgp /usr/local/bin/
COPY --from=0 /gobgpd /usr/local/bin/
ADD run.sh /run.sh
