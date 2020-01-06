FROM node:8

# Create app directory
RUN mkdir -p /usr/src/SqlToSqlDataIntgration
WORKDIR /usr/src/SqlToSqlDataIntgration

# Bundle app source
COPY . /usr/src/SqlToSqlDataIntgration

# Install app dependencies
RUN WITH_SASL=0 npm install

CMD [ "node", "index.js"]
