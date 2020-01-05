FROM node:alpine

RUN apk update && apk upgrade && \
  apk add --no-cache bash git 

WORKDIR '/project'

RUN git clone --depth=1 https://bitbucket.org/code-examples/pingvin.org .
RUN npm install

CMD ["npm", "run", "start"]