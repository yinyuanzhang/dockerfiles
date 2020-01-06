FROM node:carbon-slim

# Create app directory
WORKDIR /git/videos-api

# Install app dependencies
COPY package.json /git/videos-api/
RUN npm install

# Bundle app source
COPY . /git/videos-api/
RUN npm run prepublish

CMD [ "npm", "run", "runServer" ]

EXPOSE 5000
