FROM node:boron

# Create app directory
RUN mkdir -p /usr/src/frontend-exchanger
WORKDIR /usr/src/frontend-exchanger

# Install app dependencies
COPY package.json /usr/src/frontend-exchanger/
RUN npm install

# Bundle app source
COPY . /usr/src/frontend-exchanger

EXPOSE 8080
CMD [ "npm", "test" ]
