FROM node
# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install --production
COPY . /usr/src/app
EXPOSE 5000
WORKDIR /usr/src/app/
CMD [ "npm", "start"]