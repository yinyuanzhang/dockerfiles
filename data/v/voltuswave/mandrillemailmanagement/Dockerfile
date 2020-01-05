FROM node:10

# Create app directory
RUN mkdir -p /usr/src/MandrillEmailManagement
WORKDIR /usr/src/MandrillEmailManagement           

# Bundle app source
COPY . /usr/src/MandrillEmailManagement

# Install app dependencies
RUN WITH_SASL=0 npm install

CMD [ "node", "server.js"]


