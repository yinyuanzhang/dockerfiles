FROM node:9

ENV NODE_ENV development

WORKDIR /usr/app

COPY package.json .

RUN npm install 

COPY src src

COPY public public

CMD ["npm", "start"]
