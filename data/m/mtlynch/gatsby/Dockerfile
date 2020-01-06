FROM node:10.15.3-stretch-slim

# Install dependencies.
RUN apt-get update && \
      apt-get install --yes \
        libglu1 \
        libxi6

# Install Gatsby CLI.
RUN npm install --global gatsby-cli@2.5.4
