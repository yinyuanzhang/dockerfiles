FROM node:6-slim

ENV \
  HOME=/var/app \
  EXPRESS_PORT=3000

COPY app/ /var/app

WORKDIR /var/app

RUN \
  apt-get update && \
  apt-get install -y python-m2crypto supervisor && \
  rm -rf /var/lib/apt/lists/* && \
  sed -i 's/^\(\[supervisord\]\)$/\1\nnodaemon=true/' /etc/supervisor/supervisord.conf && \
  npm install --production yo generator-hubot coffee-script pm2 && \
  npm install && \
  npm cache clean

COPY hubot.conf /etc/supervisor/conf.d

# USER www-data

EXPOSE 3000

# Entrypoint
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
