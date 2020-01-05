FROM ubuntu
RUN apt-get update
RUN apt-get install -y wget
RUN wget -O - http://dl.hhvm.com/conf/hhvm.gpg.key | sudo apt-key add -
RUN echo deb http://dl.hhvm.com/ubuntu trusty main | sudo tee /etc/apt/sources.list.d/hhvm.list
RUN apt-get update
RUN apt-get install -y hhvm
RUN hhvm --version
