FROM finpack/scala-sbt:java_8_sbt_1.3.2_scala_2.13

ENV NVM_VERSION 0.33.8
ENV NODE_VERSION 11.9.0
ENV DOCKER_VERSION 17.03.0-ce

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Workaround for error on docker hub
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get update

ENV NVM_DIR /usr/local/nvm

# Install nvm with node and npm
RUN curl https://raw.githubusercontent.com/creationix/nvm/v$NVM_VERSION/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/v$NODE_VERSION/bin:$PATH

#Install Docker client
RUN curl -L -o /tmp/docker-$DOCKER_VERSION.tgz https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz \
    && tar -xz -C /tmp -f /tmp/docker-$DOCKER_VERSION.tgz \
    && mv /tmp/docker/* /usr/bin

RUN apt-get update &&\
    apt-get install -y python-pip sshpass &&\
    pip install awscli==1.11.76 &&\
    pip install awscli --upgrade --user &&\
	apt-get install sshpass &&\
    rm -rf /var/lib/apt/lists/*
