FROM node:9.6.1

RUN mkdir /usr/src/ibon
WORKDIR /usr/src/ibon

COPY package.json /usr/src/ibon/
RUN npm install

COPY . /usr/src/ibon

CMD ["npm","start"]

