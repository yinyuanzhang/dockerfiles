FROM circleci/ruby:2.6.3-node-browsers-legacy
LABEL maintainer="CAMPFIRE, Inc.<tech@camp-fire.jp>"

ENV PHANTOMJS_VERSION 2.1.1
ENV PATH $HOME/.local/bin:$PATH

RUN sudo npm install -g yarn
RUN curl --location --silent https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2 | sudo tar xj -C /usr --strip-components=1
RUN sudo apt-get install -y fonts-migmix python3-pip gettext
RUN sudo npm install -g jshint
RUN sudo gem update --system 2.7.4 # https://git.io/vAB1b
RUN sudo gem install bundler --no-rdoc --no-ri --force
RUN pip3 install awscli
