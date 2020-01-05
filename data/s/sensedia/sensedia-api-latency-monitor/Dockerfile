FROM node:8-alpine
LABEL Author="André Nishitani <andre.nishitani@sensedia.com>"

RUN mkdir /ws

WORKDIR /ws

RUN npm install request argparse

COPY sensedia-api-latency-monitor.js /ws

ENTRYPOINT ["node", "sensedia-api-latency-monitor.js"]

