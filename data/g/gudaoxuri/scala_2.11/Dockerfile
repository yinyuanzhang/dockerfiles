FROM gudaoxuri/java:latest
MAINTAINER gudaoxuri <i@sunisle.org>

#---------------Install Scala---------------
RUN wget -P /opt/env/ http://downloads.typesafe.com/scala/2.11.12/scala-2.11.12.tgz  && \
    tar -xzf /opt/env/scala-2.11.12.tgz -C /opt/env/  && \
    rm /opt/env/scala-2.11.12.tgz  && \
    mv /opt/env/scala-2.11.12 /opt/env/scala

RUN echo "export SCALA_HOME=/opt/env/scala" >> /etc/profile
RUN sed /^PATH=/d /etc/profile >> /etc/profile && \
   echo 'PATH=$PATH:$JAVA_HOME/bin:$SCALA_HOME/bin' >> /etc/profile

RUN echo "export SCALA_HOME=/opt/env/scala" >> /root/.bashrc

ENV SCALA_HOME /opt/env/scala
ENV PATH $PATH:$JAVA_HOME/bin:$SCALA_HOME/bin

