FROM ubuntu:18.04

LABEL authors="Piotr Kurek"

# Installing wget - needed to download node.js
RUN apt-get update && apt-get install -y wget

# Using latest LTS release.
ENV NODE_VERSION v8.11.4

# Downloading and installing Node.
RUN wget -O - https://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION-linux-x64.tar.gz \
    | tar xzf - --strip-components=1 --exclude="README.md" --exclude="LICENSE" \
    --exclude="ChangeLog" -C "/usr/local"

# Set the working directory.
WORKDIR /app

# COpying application files
ADD . /app

# Installing packages
RUN npm i --production

# When starting a container with our image, this command will be run.
CMD ["node", "worker/index.js"]
