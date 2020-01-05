FROM multiarch/alpine:arm64-latest-stable

ENV VERSION="Sakura_frpc_linux_arm" \
    USERNAME="abc" \
    PASSWD="abc" \
    SID="serverid"
# ENV ID tunnelid

RUN apk add --no-cache ca-certificates && \
    wget --no-check-certificate https://cdn.tcotp.cn:4443/client/${VERSION}.tar.gz && \ 
    tar xzf ${VERSION}.tar.gz && \
    mv ${VERSION} /sakura && \
    chmod +x /sakura && \
    rm -rf *.tar.gz /var/cache/apk/* /tmp/*

CMD exec /sakura --su=$USERNAME --sp=$PASSWD --sid=$SID --disable-pause
