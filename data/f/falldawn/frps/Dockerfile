FROM alpine:latest

ENV frps_version=0.22.0 \
    frps_DIR=/usr/local/frp

RUN set -ex && \
    frps_latest=https://github.com/fatedier/frp/releases/download/v${frps_version}/frp_${frps_version}_linux_amd64.tar.gz && \
    frps_latest_filename=frp_${frps_version}_linux_amd64.tar.gz && \
    apk add --no-cache pcre bash && \
    apk add --no-cache  --virtual TMP wget tar && \
    [ ! -d ${frps_DIR} ] && mkdir -p ${frps_DIR} && cd ${frps_DIR} && \
    wget --no-check-certificate -q ${frps_latest} -O ${frps_latest_filename} && \
    tar xzf ${frps_latest_filename} && \
    mv frp_${frps_version}_linux_amd64/frps ${frps_DIR}/frps && \
    apk --no-cache del --virtual TMP && \
    rm -rf /var/cache/apk/* ~/.cache ${frps_DIR}/${frps_latest_filename} ${frps_DIR}/frp_${frps_version}_linux_amd64

VOLUME [ "/etc/frp" ]

ENTRYPOINT ["/usr/local/frp/frps", "-c", "/etc/frp/frps.ini"]