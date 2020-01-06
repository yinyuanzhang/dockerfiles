FROM nginx:1.17

# Install certbot
RUN echo "deb http://deb.debian.org/debian stretch-backports main" >> /etc/apt/sources.list \
  && apt-get update \
  && apt-get install -y certbot python-certbot-nginx -t stretch-backports \
  && apt-get install -y python3-certbot-dns-cloudflare

# Default setting files
COPY proxy.conf /etc/nginx