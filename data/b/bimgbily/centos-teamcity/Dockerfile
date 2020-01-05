FROM bimgbily/centos-java:latest

RUN mkdir /opt/jetbrains
RUN cd /opt/jetbrains
RUN wget https://download.jetbrains.com/teamcity/TeamCity-9.1.6.tar.gz
RUN tar zxf TeamCity-9.1.6.tar.gz -C /opt/jetbrains
RUN rm TeamCity-9.1.6.tar.gz

EXPOSE 8111
CMD ["/opt/jetbrains/TeamCity/bin/teamcity-server.sh", "run"]
