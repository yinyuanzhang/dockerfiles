FROM factual/docker-cdh5-base

RUN apt-get update

# basics
RUN apt-get install -y curl wget git-core
RUN apt-get install -y build-essential
RUN apt-get install -y automake unzip zlib1g-dev libcurl4-gnutls-dev libncurses5-dev bison flex libboost-all-dev libevent-dev
RUN apt-get install -y vim python3

# ruby && rvm && bundler
# ref https://rvm.io/rvm/install
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
RUN \curl -sSL https://get.rvm.io | bash -s stable --ruby
RUN /bin/bash -l -c "rvm requirements"
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"

# nodejs && npm
# ref https://nodejs.org/en/download/package-manager
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN sudo apt-get install -y nodejs

# ldap
RUN apt-get install -y ldap-utils libpam-ldap libnss-ldap nslcd

# openjdk
RUN apt-get install -y openjdk-8-jdk-headless ant

#maven
ENV MAVEN_VERSION=3.3.9
ADD http://apache.cs.utah.edu/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz .
RUN cd /opt/ && tar xzf ../apache-maven-$MAVEN_VERSION-bin.tar.gz
RUN ln -s /opt/apache-maven-$MAVEN_VERSION/bin/mvn /usr/bin/mvn

#lein
ADD https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein /bin/lein
ENV LEIN_ROOT=true
RUN chmod 755 /bin/lein

#thrift
ENV THRIFT_VERSION=0.9.2
ADD http://www.apache.org/dist/thrift/$THRIFT_VERSION/thrift-$THRIFT_VERSION.tar.gz .
RUN tar xzf thrift-$THRIFT_VERSION.tar.gz && cd thrift-$THRIFT_VERSION && ./configure --without-ruby --without-cpp --without-nodejs --without-python && make install
RUN rm -rf thrift-$THRIFT_VERSION*

#Drake
ADD https://raw.githubusercontent.com/Factual/drake/master/bin/drake /bin/drake
RUN chmod 755 /bin/drake

#man
RUN apt-get purge -y manpages manpages-dev man-db
RUN apt-get install -y manpages manpages-dev man-db

#spark 2.0
RUN wget -O /usr/local/spark-2.0.0-bin-hadoop2.6.tgz http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0-bin-hadoop2.6.tgz
RUN tar -xzf /usr/local/spark-2.0.0-bin-hadoop2.6.tgz -C /usr/local/
RUN rm /usr/local/spark-2.0.0-bin-hadoop2.6.tgz
ENV PATH=/usr/local/spark-2.0.0-bin-hadoop2.6/bin:$PATH
ENV HADOOP_CONF_DIR=/etc/hadoop/conf
ADD spark-defaults.conf /usr/local/spark-2.0.0-bin-hadoop2.6/conf/

#cleanup
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN rm /apache-maven-*.gz

ADD bootstrap.sh /etc/my_init.d/099_bootstrap
