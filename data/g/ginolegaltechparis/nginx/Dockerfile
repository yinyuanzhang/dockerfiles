FROM nginx:stable
RUN apt-get update -y && \
apt-get install -y curl \
telnet \
net-tools && \
rm -rf /var/lib/apt/lists/*
RUN mkdir /etc/nginx/ssl && \
mkdir -p /data/nginx/log/drafter
VOLUME /data/nginx/log/drafter

EXPOSE 443
