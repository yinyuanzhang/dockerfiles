# Build:
# docker build -t meanjs/mean .
#
# Run:
# docker run -it meanjs/mean
#
# Compose:
# docker-compose up -d

# Get node 8
FROM node:8
MAINTAINER Lingga

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Set development environment as default
ENV NODE_ENV development

# Bundle app source
COPY . .

EXPOSE 3001
CMD [ "npm", "start" ]
