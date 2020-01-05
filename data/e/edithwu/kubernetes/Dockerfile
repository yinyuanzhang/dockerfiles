FROM tomcat

RUN rm -rf /usr/local/tomcat/webapps/ROOT/*
COPY build/ /usr/local/tomcat/webapps/ROOT/

COPY jdk1.8.0_191 /usr/local/jdk1.8.0_191/

ENV JAVA_HOME /usr/local/jdk1.8.0_191
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ENV PATH $PATH:$JAVA_HOME


EXPOSE 8080
