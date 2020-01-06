FROM node:boron

# Create app directory
RUN mkdir -p /home/node/app
WORKDIR /home/node/app

# Install app dependencies
COPY package.json /home/node/app
RUN npm install

# Bundle app source
COPY . /home/node/app

EXPOSE 8000

USER node

CMD [ "node", "server.js" ]
