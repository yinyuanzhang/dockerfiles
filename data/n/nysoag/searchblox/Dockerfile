FROM centos:latest
RUN yum update -y
RUN yum install java-11-openjdk-devel -y
RUN yum install -y curl
RUN yum install -y wget
WORKDIR /opt/
RUN adduser searchblox
RUN echo "searchblox:searchblox" | chpasswd
RUN wget https://d2fco3ozzrfhhd.cloudfront.net/v9.0.0/searchblox-9.0.0-1.noarch.rpm
RUN rpm -ivh searchblox-9.0.0-1.noarch.rpm
RUN chown -R searchblox:searchblox /opt/searchblox
RUN chmod -R 777 /opt/searchblox/logs
RUN chmod -R 777 /opt/searchblox/elasticsearch
RUN chmod -R 777 /opt/searchblox/bin
USER searchblox
WORKDIR /opt/searchblox/elasticsearch
CMD ./bin/elasticsearch -d && sleep 30 && cd /opt/searchblox && java -jar start.jar