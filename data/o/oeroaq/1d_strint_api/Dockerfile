FROM node:carbon-slim

# Create app directory
WORKDIR /git/strint-api

# Install app dependencies
COPY package.json /git/strint-api/
RUN npm install

# Bundle app source
COPY . /git/strint-api/
RUN npm run prepublish
#EXPOSE 8000
CMD [ "npm", "run", "runServer" ]
