FROM node:11.9.0-alpine

LABEL maintainer "nyankokota <public@nyanko-kota.com>"

RUN npm install -g redis-commander

ENTRYPOINT ["redis-commander"]

EXPOSE 8080

CMD [ "--redis-host", "redis", "--port", "8080" ]
