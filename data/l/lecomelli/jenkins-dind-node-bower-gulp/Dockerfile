FROM ubuntu:16.04

ENV JAVA_HOME /opt/jdk/jdk1.8.0_111
ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 4.6.1
ENV DIND_COMMIT 3b5fac462d21ca164b3778647420016315289034

RUN apt-get update -y       \
    && apt-get upgrade -y   \
    && apt-get install -y   \
       apt-transport-https  \
       build-essential      \
       bzip2                \
       ca-certificates      \
       curl                 \
       git                  \
       iptables             \
       jq                   \
       lvm2                 \
       lxc                  \
       unzip                \
       zip


# docker
RUN curl -sSL https://get.docker.com | sh
# fetch DIND script
RUN curl -sSL https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind -o /usr/local/bin/dind \
    && chmod a+x /usr/local/bin/dind

COPY ./wrapper.sh /usr/local/bin/wrapper.sh
RUN chmod a+x /usr/local/bin/wrapper.sh


RUN wget --header "Cookie: oraclelicense=accept-securebackup-cookie"  http://download.oracle.com/otn-pub/java/jdk/8u111-b14/jdk-8u111-linux-x64.tar.gz
RUN mkdir /opt/jdk
RUN tar -zxf jdk-8u111-linux-x64.tar.gz -C /opt/jdk
RUN update-alternatives --install /usr/bin/java java /opt/jdk/jdk1.8.0_111/bin/java 100
RUN update-alternatives --install /usr/bin/javac javac /opt/jdk/jdk1.8.0_111/bin/javac 100

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz" \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

RUN npm install -g npm 
RUN npm install -g bower
RUN npm install -g gulp 

VOLUME /var/lib/docker
ENTRYPOINT []
CMD []
