FROM node:10-alpine

# Create app directory
WORKDIR /usr/src/webapp

# Take advantage of cached Docker layers.
COPY package*.json ./
RUN npm install

# Build app
COPY . .
RUN npm run build

# Start.
CMD [ "npm", "start" ]