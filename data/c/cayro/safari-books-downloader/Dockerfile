FROM node:10-alpine

VOLUME /data/Books
WORKDIR /data

COPY ./ ./

RUN npm install && npm audit fix

ENTRYPOINT [ "node", "index.js", "-o", "/data/Books/book.epub" ]
CMD        [ "--help" ]
