FROM node:carbon

WORKDIR /usr/src/app

COPY . .

WORKDIR /usr/src/app

RUN npm install --unsafe-perm

EXPOSE 4000

CMD [ "npm", "start" ]
