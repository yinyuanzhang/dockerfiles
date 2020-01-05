# Use the official Node.js 10 image.
# https://hub.docker.com/_/node
FROM node:10

# Create and change to the app directory.
WORKDIR /usr/src/app

# Copy application dependency manifests to the container image.
# A wildcard is used to ensure both package.json AND package-lock.json are copied.
# Copying this separately prevents re-running npm install on every code change.
COPY package*.json ./

# Install production dependencies.
# RUN npm init
# RUN npm install express —-save
# RUN npm install babel-cli --save
# RUN npm install babel-preset-es2015 --save
# RUN npm run-script build


# Copy local code to the container image.
COPY . .

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 80

# Run the web service on container startup.
CMD [ "npm", "start" ]
# CMD ["echo", "helloworld"]