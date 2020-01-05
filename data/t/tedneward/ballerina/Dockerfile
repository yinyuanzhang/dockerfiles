FROM tedneward/java
MAINTAINER Ted Neward <ted@tedneward.com>

# At some point in the future, try using RPM
# curl https://product-dist.ballerina.io/downloads/0.980.1/ballerina-platform-linux-installer-x64-0.980.1.rpm to /tmp
# rpm -i /tmp/file.rpm

ENV BALLERINA_VER=0.980.1

RUN curl -fsSL -o /tmp/ballerina-tools-${BALLERINA_VER}.zip https://product-dist.ballerina.io/downloads/${BALLERINA_VER}/ballerina-platform-${BALLERINA_VER}.zip && \ 
  unzip -d /usr/local /tmp/ballerina-tools-${BALLERINA_VER}.zip

ENV BALLERINA_HOME=/usr/local/ballerina-tools-${BALLERINA_VER}
ENV PATH=$BALLERINA_HOME/bin:$PATH

EXPOSE 9090

ENTRYPOINT ["/bin/bash"]
