FROM eclipse/ubuntu_jdk8

ENV ANT_VERSION=1.10.1 \
    ANT_HOME=/home/user/apache-ant

ENV PATH=/usr/local/bin/aws:$ANT_HOME/bin:$PATH

RUN mkdir /home/user/apache-ant && \
    wget -qO- "http://archive.apache.org/dist/ant/binaries/apache-ant-$ANT_VERSION-bin.tar.gz" | tar -zx --strip-components=1 -C /home/user/apache-ant && \
    sudo chgrp -R 0 ${HOME} && \
    sudo chmod -R g+rwX ${HOME}

RUN sudo apt-get -qq update
RUN sudo apt-get -y -q install curl
RUN sudo apt-get -y -q install mercurial
RUN sudo apt-get -y -q install vim
RUN sudo apt-get -y -q install nano
RUN sudo apt-get -y -q install postgresql-client
# This is only so aws s3 help does not fail because undeclared dependencies. May not be needed.
RUN sudo apt-get -y -q install groff

RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "/home/user/awscli-bundle.zip"
RUN unzip /home/user/awscli-bundle.zip -d /home/user/
RUN sudo /home/user/awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
