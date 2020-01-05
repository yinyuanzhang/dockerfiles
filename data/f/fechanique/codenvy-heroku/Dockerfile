FROM codenvy/shellinabox
RUN sudo apt-get update && sudo apt-get install git -y
LABEL che:server:8080:ref=tomcat8 che:server:8080:protocol=http che:server:4200:ref=shellinabox che:server:4200:protocol=http
RUN wget \
    --no-cookies \
    --no-check-certificate \
    --header "Cookie: oraclelicense=accept-securebackup-cookie" \
    -qO- \
    "http://download.oracle.com/otn-pub/java/jdk/8u51-b16/jdk-8u51-linux-x64.tar.gz" | sudo tar -zx -C /opt/
     
ENV JAVA_HOME /opt/jdk1.8.0_51
RUN echo "export JAVA_HOME=$JAVA_HOME" >> /home/user/.bashrc
ENV PATH $JAVA_HOME/bin:$PATH
RUN echo "export PATH=$PATH" >> /home/user/.bashrc

EXPOSE 8080
ENV CODENVY_APP_PORT_8080_HTTP 8080

RUN mkdir -p /home/user/maven3 && \
    wget -qO- "http://archive.apache.org/dist/maven/maven-3/3.1.1/binaries/apache-maven-3.1.1-bin.tar.gz" | tar -zx --strip-components=1 -C /home/user/maven3
ENV M2_HOME /home/user/maven3   
RUN echo "export M2_HOME=$M2_HOME" >> /home/user/.bashrc
ENV PATH $M2_HOME/bin:$PATH
RUN echo "export PATH=$PATH" >> /home/user/.bashrc
#CMD tailf /dev/null

#COPY SRC

#RUN mkdir -p /home/user/app/src
#ADD $src$ /home/user/app/src/
#WORKDIR /home/user/app/src
#RUN mvn -q package
#CMD java -jar target/dependency/jetty-runner.jar target/*.war

#CMD sleep 365d
