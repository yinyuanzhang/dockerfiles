# based on the official image from microsoft
FROM mcr.microsoft.com/dotnet/core/sdk:3.1

# Install ZIP
RUN apt-get update && apt-get install zip unzip

# Install NodeJS
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get update && apt-get install -y nodejs
RUN npm rebuild node-sass

# Install WebPack
RUN npm install --global webpack
RUN npm install webpack-cli

# Install Storybook
RUN npm i -g storybook
RUN npm i -g @storybook/cli
