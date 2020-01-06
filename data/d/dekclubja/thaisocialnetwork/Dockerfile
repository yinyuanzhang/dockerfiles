FROM node:6.9.5

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

ENV PATH /usr/src/app/node_modules/.bin:$PATH

COPY . /usr/src/app/
RUN npm install --silent

CMD ["npm","run","dev"]
