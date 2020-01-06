FROM node:8.9-alpine

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json .
# For npm@5 or later, copy package-lock.json as well
# COPY package.json package-lock.json ./

RUN npm install --production

# Bundle app source
COPY . .

# Set Environment
ENV NODE_ENV=staging

# Build Angular Dist
#RUN npm run build:staging

EXPOSE 4200

CMD [ "npm", "start" ]
