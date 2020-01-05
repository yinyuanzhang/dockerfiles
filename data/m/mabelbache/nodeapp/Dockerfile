FROM node

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

ENV exposedport=8080

RUN npm install express
RUN npm install express-validator
RUN npm install dd-trace
RUN npm install winston
RUN npm install hot-shots
RUN npm install nodejs-mysql


RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .

#   ENV MYSQLADDRESS=localhost
ENV MYSQLADDRESS=192.168.63.129


EXPOSE 8081
CMD [ "npm", "start" ]