FROM alpine
MAINTAINER Hany Michael

RUN apk add --update nodejs net-tools npm

ENV NODE_ENV=production
ENV PORT=3000

COPY    . /var/www
WORKDIR /var/www
RUN     npm install
EXPOSE $PORT
ENTRYPOINT ["npm", "start"]