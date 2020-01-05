FROM nginx:stable

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && \
    apt-get install --no-install-recommends --no-install-suggests -y \
        python-certbot-nginx cron && \
    rm -rf /var/lib/apt/lists/*

COPY nginx.conf /etc/nginx/nginx.conf
COPY ssl-cron /etc/cron.d/ssl-cron
RUN crontab /etc/cron.d/ssl-cron
CMD ["sh", "-c", "nginx && cron -f"]

