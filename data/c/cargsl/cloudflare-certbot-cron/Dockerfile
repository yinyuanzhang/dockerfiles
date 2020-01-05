FROM certbot/dns-cloudflare:latest

COPY crontabs /var/spool/cron/crontabs/root
COPY certbot-renew /etc/periodic/halfday/certbot
COPY certbot-request /opt/certbot/request-cert.sh

RUN chmod +x /opt/certbot/request-cert.sh

ENTRYPOINT [ "crond", "-l", "2", "-f" ]