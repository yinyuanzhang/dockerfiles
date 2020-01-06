FROM node:carbon-slim

# Create app directory
WORKDIR /git/API_GET

# Install app dependencies
COPY package.json /git/API_GET/
RUN npm install

# Bundle app source
COPY . /git/API_GET/
RUN npm run prepublish

CMD [ "npm", "run", "runServer" ]
EXPOSE 5000
