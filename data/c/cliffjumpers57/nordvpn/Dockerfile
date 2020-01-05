FROM alpine:3.9

LABEL maintainer="Julio Gutierrez <bubuntux@gmail.com>"

COPY nordVpn.sh /usr/bin

HEALTHCHECK --timeout=15s --interval=60s\
  CMD curl -fL 'https://www.google.com' || exit 1

ENV URL_NORDVPN_API="https://api.nordvpn.com/server" \
    URL_RECOMMENDED_SERVERS="https://nordvpn.com/wp-admin/admin-ajax.php?action=servers_recommendations" \
    URL_OVPN_FILES="https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip" \
    MAX_LOAD=70

VOLUME ["/vpn"]

    # Install dependencies 
RUN apk --no-cache --no-progress update && \
    apk --no-cache --no-progress upgrade && \
    apk --no-cache --no-progress add bash curl unzip iptables ip6tables jq openvpn tini shadow  && \
    mkdir -p /vpn/ovpn

ENTRYPOINT ["/sbin/tini", "--", "/usr/bin/nordVpn.sh"]
