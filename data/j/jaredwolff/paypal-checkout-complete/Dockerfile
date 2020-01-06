# Use Node v7 as the base image.
FROM node:7

# File Author / Maintainer
MAINTAINER Jared Wolff

# Provides cached layer for node_modules
ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN mkdir -p /app && cp -a /tmp/node_modules /app/

# Define working directory
WORKDIR /app
# Add everything in the current directory to our image, in the 'app' folder.
ADD . /app

# Expose port
EXPOSE 3000

# Run our app.
CMD ["node","/app/node_modules/micro/bin/micro.js"]