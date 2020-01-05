FROM centos:7

RUN yum update -y && \
    yum install -y java-1.8.0 java-devel wget

#RUN java --version

WORKDIR /usr/local

RUN wget http://www-us.apache.org/dist/tomcat/tomcat-9/v9.0.14/bin/apache-tomcat-9.0.14.tar.gz && \
    tar -xvf apache-tomcat-9.0.14.tar.gz && \
        mv apache-tomcat-9.0.14 tomcat && \
        rm -rf  apache-tomcat-9.0.14.tar.gz

RUN echo "export CATALINA_HOME="/usr/local/tomcat"" >> ~/.bashrc && \
    source ~/.bashrc
EXPOSE 8080
CMD ["tomcat/bin/catalina.sh", "run"]
