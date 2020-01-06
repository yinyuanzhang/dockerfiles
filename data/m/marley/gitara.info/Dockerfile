FROM node:alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git 

WORKDIR '/project'

RUN git clone https://bitbucket.org/code-examples/gitara.info .
RUN npm install

CMD ["npm", "run", "start"]