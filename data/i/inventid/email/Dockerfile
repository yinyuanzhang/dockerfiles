FROM node:8.5
MAINTAINER inventid

EXPOSE 3000

RUN mkdir -p /usr/src/app/src
RUN groupadd -r maily && useradd -r -g maily -d /usr/src/app maily
RUN chown maily:maily /usr/src/app
RUN yarn global add install babel-cli babel-preset-es2015 babel-preset-react

USER maily
WORKDIR /usr/src/app

COPY yarn.lock /usr/src/app
COPY package.json /usr/src/app/
RUN yarn install
COPY index.js /usr/src/app/src/
COPY .babelrc /usr/src/app/src/
COPY components /usr/src/app/src/components
RUN cd /usr/src/app/src && babel . --out-dir ../

CMD [ "node", "index.js" ]
