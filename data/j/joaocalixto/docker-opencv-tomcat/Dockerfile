FROM henen/jdk8-tomcat8-opencv

MAINTAINER Calixto <joao.chagas@neurotech.com.br>

#/opt/opencv-2.4.7/sources/data
RUN wget -q https://www.dropbox.com/s/exuoayxj3ju8fds/data.tar.gz?dl=0 -O $(pwd)/dataSouce.tar.gz
RUN mkdir -p /opt/opencv-2.4.7/sources/data
RUN tar -xvf $(pwd)/dataSouce.tar.gz -C /opt/opencv-2.4.7/sources/data/
RUN rm $(pwd)/dataSouce.tar.gz

# opencv loader
RUN wget -q https://www.dropbox.com/s/ipne1yvcrbixd1h/face-opencv-loader-2.0.1.jar?dl=0 -O $(pwd)/face-opencv-loader-2.0.1.jar
RUN mv $(pwd)/face-opencv-loader-2.0.1.jar /opt/tomcat/lib

# opencv loader
RUN wget -q https://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.34/mysql-connector-java-5.1.34.jar
RUN mv $(pwd)/mysql-connector-java-5.1.34.jar /opt/tomcat/lib


RUN echo Fim
