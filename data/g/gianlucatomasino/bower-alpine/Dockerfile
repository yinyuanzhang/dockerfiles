FROM node:6-alpine
MAINTAINER gianluca.tomasino@gmail.com
RUN apk add --update git
RUN npm install -g bower

ENTRYPOINT ["bower"]
CMD ["--version"]
WORKDIR /src
