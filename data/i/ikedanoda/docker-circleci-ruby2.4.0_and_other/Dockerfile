FROM circleci/ruby:2.4-stretch-node

USER circleci

ENV RUBY_VERSION=2.4.0
ENV RUBYOPT -EUTF-8

RUN sudo apt-get install -y rbenv ruby-build

RUN echo 'eval "$(rbenv init -)"' | sudo tee -a /etc/profile.d/rbenv.sh

RUN rbenv install $RUBY_VERSION
RUN rbenv rehash
RUN rbenv global $RUBY_VERSION

RUN sudo apt-get install -y default-jdk
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" | sudo tee -a /etc/profile.d/java.sh
RUN rbenv exec gem update --system 2.7.4 # https://git.io/vAB1b
RUN rbenv exec gem install bundler --no-rdoc --no-ri
