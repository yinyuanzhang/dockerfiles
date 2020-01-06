FROM node:10.16-jessie

# Update NPM.
RUN npm install npm@latest -g

# Show current node version.
RUN node -v
RUN npm -v

# Install other needed stuff.
RUN apt-get update && apt-get install --no-install-recommends -y \
        wget \
        vim \
        git \
        unzip \
        openssh-client \
        rsync \
        gnupg2
