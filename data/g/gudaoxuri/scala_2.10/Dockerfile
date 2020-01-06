FROM gudaoxuri/java:latest
MAINTAINER gudaoxuri

#---------------Install Scala---------------
RUN wget -P /opt/env/ http://downloads.typesafe.com/scala/2.10.6/scala-2.10.6.tgz  && \
    tar -xzf /opt/env/scala-2.10.6.tgz -C /opt/env/  && \
    rm /opt/env/scala-2.10.6.tgz  && \
    mv /opt/env/scala-2.10.6 /opt/env/scala  && \
    echo "export SCALA_HOME=/opt/env/scala" >> /etc/profile
ENV SCALA_HOME /opt/env/scala

RUN sed /^PATH=/d /etc/profile >> /etc/profile && \
   echo 'PATH=$PATH:$JAVA_HOME/bin:$SCALA_HOME/bin' >> /etc/profile
ENV PATH $PATH:$JAVA_HOME/bin:$SCALA_HOME/bin