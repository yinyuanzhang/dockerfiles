FROM node:8.15.0

#
WORKDIR /Users/next-docker

#install package

COPY package*.json ./

RUN npm install

# copy source file

COPY . .

#Build app

RUN npm run build

#Running  app

CMD ["npm", "start"]
