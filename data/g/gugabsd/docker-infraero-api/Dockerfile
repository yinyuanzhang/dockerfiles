FROM node:8-alpine

RUN mkdir -p /infraero \
  && apk --update --no-cache add git \
  && cd /infraero \
  && git clone https://github.com/luicaps/infraero-wsdl-http.git \
  && cd infraero-wsdl-http \
  && npm install \
  && apk del git

CMD node /infraero/infraero-wsdl-http/app.js

