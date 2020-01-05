FROM jitsi/base

RUN apt update && \
    apt install -y gnupg2 curl && \
    echo "deb [trusted=yes] http://nginx.org/packages/mainline/debian stretch nginx" | tee /etc/apt/sources.list.d/nginx.list && \
    curl -fsSL https://nginx.org/keys/nginx_signing.key | apt-key add - && \
    apt-cleanup

RUN \
	apt-dpkg-wrap apt-get update && \
	apt-dpkg-wrap apt-get install -y cron nginx-dbg/stable jitsi-meet-web && \
	apt-dpkg-wrap apt-get install -y -t stretch-backports certbot && \
	apt-cleanup && \
	rm -f /etc/nginx/conf.d/default.conf && \
	rm -f /usr/share/jitsi-meet/interface_config.js

COPY rootfs/ /

EXPOSE 80 443

VOLUME ["/config", "/etc/letsencrypt"]
