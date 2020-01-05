FROM library/openjdk:jdk

ENV NODE_VERSION=6.11.0
ENV LEIN_VERSION=2.7.1
ENV LEIN_INSTALL=/usr/local/bin/
ENV LEIN_ROOT=1
ENV PATH=$PATH:/usr/local/yarn/bin
RUN \
  wget https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz && \
  tar -xJf node-v$NODE_VERSION-linux-x64.tar.xz -C /usr/local --strip-components=1 && \
  rm node-v$NODE_VERSION-linux-x64.tar.xz && \
  ln -sf /usr/local/bin/node /usr/local/bin/nodejs && \
  cd /usr/local/ && \
  mkdir -p /usr/local/yarn && \
  wget https://yarnpkg.com/latest.tar.gz && \
  tar -zvxf latest.tar.gz -C /usr/local/yarn --strip-components=1 && \
  rm /usr/local/latest.tar.gz && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y maven &&\
  cp /etc/ssl/certs/java/cacerts /tmp/jssecacerts && \
  wget "https://s3-us-west-2.amazonaws.com/jsse-ca-certs/csaa-root-cert.crt" -O /tmp/csaa-root-cert.crt && \
  wget "https://s3-us-west-2.amazonaws.com/jsse-ca-certs/csaa-issuing-cert.crt" -O /tmp/csaa-issuing-cert.crt && \
  keytool -noprompt -import -trustcacerts -alias csaa-root -file /tmp/csaa-root-cert.crt -keystore /tmp/jssecacerts -storepass changeit && \
  keytool -noprompt -import -trustcacerts -alias csaa-issuing -file /tmp/csaa-issuing-cert.crt -keystore /tmp/jssecacerts -storepass changeit && \
  cp -avv /tmp/jssecacerts $JAVA_HOME/jre/lib/security/jssecacerts && \
  mkdir -p $LEIN_INSTALL && \
  cd $LEIN_INSTALL && \
  wget "https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein" && \
  chmod +x lein && \
  lein
