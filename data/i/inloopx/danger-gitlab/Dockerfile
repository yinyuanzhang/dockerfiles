FROM ubuntu:16.04
MAINTAINER Jakub Knejzlik <jakub.knejzlik@inloopx.com>
MAINTAINER Radim Halfar <radim.halfar@inloopx.com>

# Install dependencies
RUN apt-get update && apt-get install -y git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties software-properties-common libffi-dev nodejs rubygems ruby-dev make gcc git

# Update git to newer version
RUN add-apt-repository ppa:git-core/ppa
RUN apt-get update && apt-get install -y git

# Install Ruby
RUN git clone https://github.com/rbenv/rbenv.git /usr/local/.rbenv
ENV PATH /usr/local/.rbenv/bin:$PATH
RUN eval "$(rbenv init -)"

# Install ruby build
RUN git clone https://github.com/rbenv/ruby-build.git /usr/local/.rbenv/plugins/ruby-build
ENV PATH /usr/local/.rbenv/plugins/ruby-build/bin:$PATH
RUN git clone https://github.com/rbenv/rbenv-gem-rehash.git /usr/local/.rbenv/plugins/rbenv-gem-rehash

# Setup ruby global version
RUN rbenv install 2.4.1
RUN rbenv global 2.4.1

# Setup bash as default shell
RUN chsh -s /bin/bash

# installing plugins
RUN gem install bundler rake
RUN gem install danger-gitlab
RUN gem install specific_install
RUN gem specific_install https://github.com/radimhalfar/danger-jira

ENV WORKDIR="/danger"

RUN danger --version

WORKDIR ${WORKDIR}

ENTRYPOINT [""]