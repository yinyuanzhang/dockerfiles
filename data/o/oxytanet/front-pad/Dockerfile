FROM node:11-alpine

RUN mkdir -p /build /opt/etherpad-lite/src/templates /opt/etherpad-lite/src/static/custom

ADD . /build/

RUN cd /build \
 && npm set progress=false \
 && npm i \
 && npm run css \
 && mv index.html /opt/etherpad-lite/src/templates  \
 && mv static/custom/index.css /opt/etherpad-lite/src/static/custom \
 && rm -rf /build
