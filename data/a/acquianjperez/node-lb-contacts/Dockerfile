FROM node

# Create app directory
RUN mkdir -pv /usr/src/node-lb-contacts
WORKDIR /usr/src/node-lb-contacts/

# Install app dependencies
COPY package.json /usr/src/node-lb-contacts/package.json
RUN npm install loopback-connector-redis --save
RUN npm install

# Bundle app source
COPY . /usr/src/node-lb-contacts

EXPOSE 3000
CMD [ "node", "." ]
