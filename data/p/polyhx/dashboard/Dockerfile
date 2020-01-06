FROM node:10-alpine

# Create app directory
RUN mkdir -p /usr/src/webapp
WORKDIR /usr/src/webapp

ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN cp -a /tmp/node_modules /usr/src/webapp

# Bundle app source
ADD . /usr/src/webapp
RUN npm run staging

EXPOSE 4000
CMD [ "npm", "run", "server" ]
