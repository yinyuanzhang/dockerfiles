FROM node:8

# Create app directory
RUN mkdir -p /usr/src/Integarations
WORKDIR /usr/src/Integarations

# Bundle app source
COPY . /usr/src/Integarations

# Install app dependencies
RUN WITH_SASL=0 npm install


# EXPOSE 3000
CMD [ "node", "integrations.js"]