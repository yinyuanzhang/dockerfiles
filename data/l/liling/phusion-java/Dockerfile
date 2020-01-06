FROM liling/phusion-fundamental:0.9.18.1
MAINTAINER lilingv@gmail.com

RUN apt-get update; apt-get install -y openjdk-7-jdk libmysql-java

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
