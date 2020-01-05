FROM certbot/certbot

COPY certbot-dns-cloudflare/ src/certbot-dns-cloudflare
COPY certbot-nginx/ src/certbot-nginx

RUN pip install --no-cache-dir --editable src/certbot-dns-cloudflare
RUN pip install --no-cache-dir --editable src/certbot-nginx
