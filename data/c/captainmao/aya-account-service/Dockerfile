FROM node:12

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install cnpm -g --registry=https://registry.npm.taobao.org
RUN cnpm install
# If you are building your code for production
# RUN npm install --only=production

# Bundle app source
COPY . .

# TODO For production
RUN npm run build

EXPOSE 8052
CMD [ "npm", "run", "start" ]