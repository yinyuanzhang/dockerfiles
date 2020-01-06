FROM node:8
MAINTAINER kulasekarapandiyan@gmail.com
ENV NODE_ENV=dev
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3002
CMD ["npm","start"]
