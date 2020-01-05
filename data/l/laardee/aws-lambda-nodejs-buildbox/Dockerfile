# https://docs.aws.amazon.com/lambda/latest/dg/current-supported-versions.html

FROM library/amazonlinux:2017.03.1.20170812

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION v6.10.3

RUN /bin/bash -c 'curl https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash \
  && source $NVM_DIR/nvm.sh \
  && nvm install $NODE_VERSION'

ENV NODE_PATH $NVM_DIR/versions/node/$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/$NODE_VERSION/bin:$PATH

RUN npm install -g aws-sdk@2.176.0
