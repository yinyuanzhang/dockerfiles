FROM node:8

# Create app directory
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

RUN npm install -g pm2
# Bundle app source
COPY . .
#EXPOSE 3600

