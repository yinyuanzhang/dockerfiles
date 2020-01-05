FROM selenium/node-chrome:latest

RUN sudo apt-get install curl 
RUN curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -

USER root
RUN wget https://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN sudo mv chromedriver /usr/bin/chromedriver

USER seluser

RUN sudo apt-get install nodejs
RUN sudo npm install -g lerna
RUN sudo npm install -g mocha

VOLUME /app
WORKDIR /app
