# Anything beyond local dev should pin this to a specific version at https://hub.docker.com/_/node/
FROM node:8 as builder

ENV CLARK_DB_NAME cart-service

# install dependencies in a different location for easier app bind mounting for local development
WORKDIR /opt/app
COPY package.json package-lock.json* jest.config.js tsconfig.json ./
RUN mkdir test_environment
COPY test_environment ./test_environment
RUN npm install && npm cache clean --force
ENV PATH /opt/node_modules/.bin:$PATH
COPY . /opt/app

CMD [ "npm", "start" ] 


