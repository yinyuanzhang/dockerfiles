FROM timbru31/node-alpine-git

ENV API_DEVOPS_VERSION 0.0.1

RUN cd /home/node && git clone --branch=master https://c1ac4cee915e06dbd7f8b190bb5b6785cf8d97fa@github.com/sileax/api-devops.git
RUN export NODE_ENV="development_postgres"
RUN cd home/node/api-devops && yarn
RUN yarn global add forever
RUN apk add --no-cache curl
CMD cd home/node/api-devops && yarn start