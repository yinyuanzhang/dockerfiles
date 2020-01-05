FROM ubuntu:latest

# RUN mv /etc/apt/sources.list /etc/apt/sources.list_backup
# COPY ./sources.list /etc/apt/sources.list
RUN apt-get -y install software-properties-common 
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update -y

# http://stackoverflow.com/questions/19275856/auto-yes-to-the-license-agreement-on-sudo-apt-get-y-install-oracle-java7-instal/19391042
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections
RUN apt-get install -y oracle-java8-installer oracle-java8-set-default
RUN apt-get install -y nodejs npm

RUN ln -s /usr/bin/nodejs /usr/bin/node

#COPY ./test /test
#RUN cd /test; npm install;
EXPOSE 3000
#COPY ./start.sh /start.sh
#CMD ["sh", "/start.sh"]
CMD ["java", "-version"]                          
