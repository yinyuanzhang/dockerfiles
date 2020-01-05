FROM node:latest

MAINTAINER Nam Trung <namtrung804@gmail.com>

# Global install yarn package manager
RUN apt-get update && apt-get install -y curl apt-transport-https && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get install -y yarn && yarn -v
# Install package create thumbnail for video
RUN apt-get install -y ffmpeg frei0r-plugins

RUN npm install -g gulp svgo

RUN npm install express-generator -g && npm install -g sequelize-cli && npm install -g node-gyp

EXPOSE 8000-9999

WORKDIR /app
