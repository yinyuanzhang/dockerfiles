#
# Dockerfile
#
#

# Use node.js version 6 base image
FROM node:6

MAINTAINER Eki Baskoro

# Install pre-requisites
RUN npm install --global gulp-cli

# Create app directory
ENV APP_DIR /usr/src/app
RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

# Copy the source files
ADD src src

# Install dependencies
ADD package.json package.json
RUN npm install

# Build the Application
ADD .babelrc .babelrc
ADD gulpfile.babel.js gulpfile.babel.js
RUN gulp build

EXPOSE 9999

CMD [ "npm", "start" ]
