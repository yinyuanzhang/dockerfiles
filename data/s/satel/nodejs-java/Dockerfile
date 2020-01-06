FROM node:8.14

RUN apt-get update -q -q && apt-get -y install openjdk-8-jdk-headless zip
RUN wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip &&\
    unzip chromedriver_linux64.zip &&\
    mv chromedriver /usr/bin/chromedriver && chown root:root /usr/bin/chromedriver &&\
    chmod +x /usr/bin/chromedriver
