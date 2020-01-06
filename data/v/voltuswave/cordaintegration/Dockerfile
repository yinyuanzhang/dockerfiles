FROM node:10

# Create app directory
RUN mkdir -p /usr/src/CordaIntegration
WORKDIR /usr/src/CordaIntegration

# Bundle app source
COPY . /usr/src/CordaIntegration

# Install app dependencies
RUN WITH_SASL=0 npm install

RUN apt-get update \
    && apt-get install -y librdkafka1 librdkafka-dev 
    

EXPOSE 13370
CMD [ "node", "server.js"]
