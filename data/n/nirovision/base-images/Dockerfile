FROM nirovision/base-images:x86_64-ubuntu16.04

# use bash to source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# install NVM
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 10.14.0
RUN mkdir -p $NVM_DIR
RUN curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
RUN source $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y --no-install-recommends yarn && rm -rf /var/lib/apt/lists/*