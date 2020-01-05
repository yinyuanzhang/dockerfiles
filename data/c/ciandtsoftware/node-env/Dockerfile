FROM ubuntu:latest

MAINTAINER CI&T-KO-TEAM

RUN apt-get update \
 && apt-get install -y curl ruby-full \
 && rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get install -y nodejs
RUN gem install sass
RUN npm install -g grunt-cli

RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

RUN mkdir -p /content/htdocs && \
 mkdir -p /content/web_resources

WORKDIR /content/web_resources

RUN echo "#!/bin/bash" > /run.sh
RUN echo "npm install && grunt docker" >> /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
