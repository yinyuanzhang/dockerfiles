FROM openjdk:11

#Versions
# Get updates from:
# - https://github.com/cloudfoundry/cli/releases
# - https://nodejs.org/en/
# - https://yarnpkg.com/lang/en/
ENV CF_CLI 6.48.0 
ENV NODE_VERSION 12.13.1
ENV YARN_VERSION 1.21.1

# Install Cloud Foundry CLI
RUN set -ex \
  && wget -qO /tmp/cf-cli.tgz "https://cli.run.pivotal.io/stable?release=linux64-binary&version=$CF_CLI" \
  && mkdir -p /usr/local/bin \
  && tar -xzf /tmp/cf-cli.tgz -C /usr/local/bin \
  && cf --version \
  && rm -f /tmp/cf-cli.tgz

# add the Blue Green Deployment plugin
RUN set -ex \
  && cf add-plugin-repo CF-Community https://plugins.cloudfoundry.org \
  && cf install-plugin blue-green-deploy -f -r CF-Community

# Install Node.js
RUN set -ex \
  # use keys from https://github.com/nodejs/node#release-keys
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 4ED778F539E3634C779C87C6D7062848A1AB005C \
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B9E2F5981AA6E0CD28160D9FF13993A75599653C \
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B9AE9905FFD7803F25714661B63B535A4C206CA9 \
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 77984A986EBC2AA786BC0F66B01FBB92821C587A \
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys FD3A5288F042B6850C66B31F09FE44734EB7990E \
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600 \
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
  && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys A48C2BEE680E841632CD4E44F07496B3EB3C1762 \
  && groupadd --gid 1000 node \
  && useradd --uid 1000 --gid node --shell /bin/bash --create-home node \
  && ARCH= && dpkgArch="$(dpkg --print-architecture)" \
  && case "${dpkgArch##*-}" in \
    amd64) ARCH='x64';; \
    ppc64el) ARCH='ppc64le';; \
    s390x) ARCH='s390x';; \
    arm64) ARCH='arm64';; \
    armhf) ARCH='armv7l';; \
    i386) ARCH='x86';; \
    *) echo "unsupported architecture"; exit 1 ;; \
  esac \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.xz" \
  && curl -SLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 --no-same-owner \
  && rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

# Install Yarn
RUN set -ex \
  && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --import \
  && curl -fSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \
  && curl -fSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \
  && gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \
  && mkdir -p /opt/yarn \
  && tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \
  && ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \
  && ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \
  && rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz

# Install Tools
RUN set -ex \
  && apt-get update  \
  && apt-get install -y libxml2-utils  \
  && apt-get install -y bc \
  && apt-get install -y jq \
  # Install latest chrome package, which installs the necessary libs to make the bundled version of Chromium that Puppeteer installs work.
  && apt-get install -y chromium \ 
  && apt-get install -y libatk-bridge2.0-0 \
  && apt-get install -y libgtk-3-0 \
  # Chromium end
  && apt-get install -y python3-dev \
  && curl -O https://bootstrap.pypa.io/get-pip.py \
  && python3 get-pip.py

# Install Python modules
RUN set -ex \
  && pip install awscli \
  && pip install requests

RUN set -ex \
    && wget -qO /usr/sbin/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x /usr/sbin/wait-for-it.sh
