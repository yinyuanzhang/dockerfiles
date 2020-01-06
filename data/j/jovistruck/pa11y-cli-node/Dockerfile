FROM node:5
MAINTAINER Joviano Dias <joviano.dias@springer.com>

# Install PhantomJS
# With DEPENDENCIES - Includes make inside build-essential + other deps for phantomjs
RUN apt-get update
RUN apt-get install -y curl apt-utils bzip2 libfreetype6 libfontconfig build-essential
RUN npm install phantomjs-prebuilt@2 -g

# Install Pa11y
RUN npm install -g pa11y
