FROM ubuntu:14.04
MAINTAINER Daisuke Shiamda

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN \
  apt-get update && \
  apt-get install -y nodejs npm ruby curl git apt-transport-https

# Install locale ja_JP
RUN \
  apt-get install -y language-pack-ja && \
  export LANG=ja_JP.UTF-8  && \
  update-locale LANG=ja_JP.UTF-8

# Install Java
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  apt-get install -y software-properties-common && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer

# Install Scala
RUN \
  cd /root && \
  wget www.scala-lang.org/files/archive/scala-2.11.7.deb && \
  dpkg -i scala-2.11.7.deb

# Install sbt
RUN \
  echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list && \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 && \
  apt-get update && \
  apt-get install sbt

RUN sbt sbt-version
RUN npm install -g typescript
RUN gem install sass
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python
RUN pip install --user codecov
RUN echo 'export PATH=$PATH:~/.local/bin/' >> /root/.bashrc

WORKDIR /
RUN rm -rf ~/.ivy2/cache/
RUN apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/*

