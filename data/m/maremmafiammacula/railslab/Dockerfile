FROM ruby:2.5.1
RUN apt update
RUN apt install curl libmagic-dev wget sshpass -yqq
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y nodejs
RUN gem install bundler --no-ri --no-rdoc
