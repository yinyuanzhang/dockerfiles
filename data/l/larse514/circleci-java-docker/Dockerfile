FROM circleci/openjdk:8u181-jdk-node-browsers
MAINTAINER andrew.larsen@vernonsoftwaresolutoins.com

#install nodejs
RUN curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
RUN sudo apt-get install -y nodejs

#Install newman 
RUN sudo npm install newman -g

# Install awscli
# http://docs.aws.amazon.com/cli/latest/userguide/awscli-install-bundle.html
RUN sudo wget "s3.amazonaws.com/aws-cli/awscli-bundle.zip" -O "awscli-bundle.zip" && \
    sudo unzip awscli-bundle.zip && \
    # Workaround to get awscli to work properly
    # https://github.com/aws/aws-cli/issues/1957#issuecomment-271057166
    sudo apt-get install groff-base && \
    sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
    sudo rm awscli-bundle.zip && \
    sudo rm -rf awscli-bundle


#Install docker
RUN set -x \
    VER="17.12.1-ce" \
    curl -L -o /tmp/docker-$VER.tgz https://download.docker.com/linux/static/stable/x86_64/docker-$VER.tgz \
    tar -xz -C /tmp -f /tmp/docker-$VER.tgz \
    mv /tmp/docker/* /usr/bin

#Install make
RUN sudo apt-get install --reinstall make

WORKDIR /
