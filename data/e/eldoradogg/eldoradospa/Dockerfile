# Base image
FROM node:10.16.0

# Install Azure CLI
# Docs https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Install chrome for protractor tests
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update && apt-get install -yq google-chrome-stable

# Install Firebase CLI
RUN npm install -g firebase-tools

# Install Sentry CLI
RUN curl -sL https://sentry.io/get-cli/ | bash

# Install Zip
RUN apt-get update && apt-get install zip

# Set working directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# Add app
COPY . /usr/src/app