FROM node
# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
# Install app dependencies nodejs
COPY package.json /usr/src/app/
RUN npm install  --allow-root
RUN npm install -g bower --allow-root
# Install app dependencies bower
COPY bower.json /usr/src/app/
RUN bower install  --allow-root
# Bundle app source
COPY . /usr/src/app

EXPOSE 8000
CMD [ "node", "index.js" ]