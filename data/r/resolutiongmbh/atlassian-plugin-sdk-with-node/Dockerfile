FROM openjdk:8-jdk

# Maintainers on this project are the following:
MAINTAINER Tobias Theobald <t.theobald@resolution.de>

RUN apt-get update \
    && apt-get install -y apt-transport-https nano less vim xmlstarlet

# Install the Atlassian Plugins SDK using the official Aptitude debian
# package repository and patch the settings.xml to work with the new OpenJDK classloading style for surefire
RUN echo "deb https://packages.atlassian.com/atlassian-sdk-deb stable contrib" >> /etc/apt/sources.list \
    && wget https://packages.atlassian.com/api/gpg/key/public \
    && apt-key add public \
    && rm public \
    && apt-get update \
    && apt-get install -y atlassian-plugin-sdk \
    && xmlstarlet ed --inplace -N "my=http://maven.apache.org/SETTINGS/1.0.0" -s "/my:settings/my:profiles/my:profile/my:properties" --type elem -n "argLine" -v "-Djdk.net.URLClassPath.disableClassPathURLCheck=true" /usr/share/atlassian-plugin-sdk-*/apache-maven-*/conf/settings.xml

# Copy Maven preference files to predefine the command line question about
# subscribing to the mailing list to `NO`.
COPY resources/.java /root/.java

# Install Node.js for web development dependencies
ARG NODE_MAJOR_VERSION="8"
ENV NODE_MAJOR_VERSION=${NODE_MAJOR_VERSION}

RUN curl -sL https://deb.nodesource.com/setup_${NODE_MAJOR_VERSION}.x | bash - \
    && apt-get install -y nodejs jq \
    && npm install -g npm@latest \
    && echo '//registry.npmjs.org/:_authToken=${NPM_TOKEN}' > ~/.npmrc

# Install yarn for Node.js package handling
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y yarn \
    && yarn --version

# Install Heroku CLI
RUN curl https://cli-assets.heroku.com/install-ubuntu.sh | sh

# Install AWS CLI
RUN apt-get install -y awscli

# Install Rancher CLI
ENV RANCHER_VERSION=v2.3.0
RUN curl -Lso /tmp/rancher.tar.gz https://github.com/rancher/cli/releases/download/${RANCHER_VERSION}/rancher-linux-amd64-${RANCHER_VERSION}.tar.gz && \
  cd /tmp && \
  tar xzf /tmp/rancher.tar.gz --strip-components=2 && \
  mv /tmp/rancher /usr/local/bin/rancher && \
  rm /tmp/rancher.tar.gz

# Create directory for sources using the same practice as the ruby images
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy helper scripts
ENV IMAGESCRIPTS_DIR=/opt/imagescripts
COPY imagescripts ${IMAGESCRIPTS_DIR}

# Set the default running command of the AMPS image to be running the
# application in debug mode.
CMD ["atlas-version"]
