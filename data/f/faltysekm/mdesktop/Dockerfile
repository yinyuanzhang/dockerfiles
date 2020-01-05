FROM node:8-alpine

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install

# If you are building your code for production
# RUN npm install --only=production

# Bundle app source
COPY . .

# Build client
RUN npm run build

# Cleanup dev mess
RUN npm prune --only=production

EXPOSE 8080
CMD [ "npm", "start" ]
