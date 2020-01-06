FROM node:10-alpine

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1

RUN npm install -g reveal-md@2.0.6

VOLUME /srv/www
WORKDIR /srv/www

EXPOSE 1948

ENTRYPOINT ["reveal-md"]
