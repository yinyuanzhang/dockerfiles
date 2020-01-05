FROM node:alpine

RUN npm install -G pug-cli jstransformer-markdown-it

VOLUME [ "/work" ]

COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
