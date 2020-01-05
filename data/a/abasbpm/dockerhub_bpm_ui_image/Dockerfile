FROM node

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre/

RUN apt-get update
RUN apt-get install -y xvfb yarn openjdk-8-jdk bash

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install google-chrome-stable \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN yarn global add polymer-cli bower && \
    yarn cache clean && \
    rm -rf /var/cache/apk/* /tmp/*
    
RUN echo '{ "allow_root": true }' > /root/.bowerrc