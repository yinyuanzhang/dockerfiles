FROM fedora:latest
RUN dnf -y update && dnf install -y cronie-anacron stress htop
RUN mkdir -p /app
COPY stress.sh /app
ADD crontab /etc/cron.d/stress
RUN chmod +x /etc/cron.d/stress
RUN chmod +x /app/stress.sh
RUN crontab /etc/cron.d/stress
CMD tail -f /dev/null
