FROM gudaoxuri/ssh:latest
MAINTAINER gudaoxuri <i@sunisle.org>

#---------------Install Java---------------
RUN wget -P /opt/env/ --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie"  http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-linux-x64.tar.gz  && \
    tar -xzf /opt/env/jdk-8u161-linux-x64.tar.gz -C /opt/env/  && \
    rm /opt/env/jdk-8u161-linux-x64.tar.gz  && \
    mv /opt/env/jdk1.8.0_161 /opt/env/java

RUN echo "export JAVA_HOME=/opt/env/java" >> /etc/profile
RUN echo 'export PATH=$PATH:$JAVA_HOME/bin' >> /etc/profile

RUN echo "export JAVA_HOME=/opt/env/java" >> /root/.bashrc

ENV JAVA_HOME /opt/env/java
ENV PATH $PATH:$JAVA_HOME/bin
