FROM node:9.6.1

WORKDIR /usr/src/labellab/labellab-client

ENV PATH /usr/src/labellab/labellab-client/node_modules/.bin:$PATH

COPY package.json /usr/src/labellab/labellab-client/package.json

RUN npm install

RUN npm install -g @angular/cli@1.7.1

COPY . /usr/src/labellab/labellab-client

CMD ng serve --host 0.0.0.0