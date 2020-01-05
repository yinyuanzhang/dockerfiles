FROM node:12-alpine

VOLUME ["/aglio"]

WORKDIR /aglio

RUN yarn global add aglio

EXPOSE 3000

ENTRYPOINT [ "/usr/local/bin/aglio" ]
