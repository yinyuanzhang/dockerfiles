FROM node:10.4.1

WORKDIR /usr/src/app
COPY package.json .
RUN npm install

EXPOSE 3000
CMD [ "npm", "start" ]

COPY . .