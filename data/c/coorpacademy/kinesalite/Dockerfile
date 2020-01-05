FROM node:10-alpine

EXPOSE 4567

ARG KINESALITE_VERSION=v1.14.0

RUN npm install -g kinesalite@${KINESALITE_VERSION}

ENTRYPOINT ["kinesalite"]
