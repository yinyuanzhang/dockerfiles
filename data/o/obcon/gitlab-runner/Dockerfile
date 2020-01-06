FROM gitlab/gitlab-runner:latest

MAINTAINER Marco Obermeyer "marco.obermeyer@obcon.de"

RUN apt-get update && \
  apt-get -y install python-pip postgresql-server-dev-9.3 python-dev libfontconfig1

RUN pip install nose mock jsonschema psycopg2 boto3 awscli

RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get install -y nodejs
RUN  apt-get autoremove -y && \
  rm -rf /var/lib/apt/lists/*
RUN npm install -g phantomjs

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
RUN sudo apt-get update && sudo apt-get install yarn
