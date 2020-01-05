FROM ubuntu:17.10

RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y \
  libreoffice pandoc openjdk-8-jdk wget \
  && rm -rf /var/lib/apt/lists/*

ENV LEIN_VERSION=2.8.1
ENV LEIN_INSTALL=/usr/local/bin/
ENV PATH=$PATH:$LEIN_INSTALL
ENV LEIN_ROOT 1
ENV LEIN_HOME /lein

RUN mkdir -p $LEIN_INSTALL \
  && wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein -O $LEIN_INSTALL/lein \
  && chmod 0755 $LEIN_INSTALL/lein \
  && mkdir $LEIN_HOME \
  && chmod 0777 $LEIN_HOME \
  # Install clojure 1.8.0 so users don't have to download it every time
  && echo '(defproject dummy "" :dependencies [[org.clojure/clojure "1.8.0"]])' > project.clj \
  && lein deps && rm project.clj
