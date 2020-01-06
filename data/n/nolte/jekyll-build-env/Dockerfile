#FROM ruby:2.4.1-jessie
FROM ruby:2.4.1-slim-jessie

ENV PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"
ENV PLANTUML_VERSION=1.2017.19

RUN export LANG=en_US.UTF-8
RUN export LANGUAGE=en_US.UTF-8
RUN export LC_ALL=en_US.UTF-8



RUN apt-get update && apt-get install build-essential chrpath libssl-dev libxft-dev \
  libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev -y

WORKDIR /tmp
RUN cd /tmp
ADD https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 /tmp/$PHANTOM_JS.tar.bz2
RUN tar -xvjf $PHANTOM_JS.tar.bz2
RUN mv $PHANTOM_JS /usr/local/share
RUN ln -s /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin
RUN phantomjs --version


RUN apt-get update && apt-get install openjdk-7-jre ditaa graphviz nodejs libcurl4-openssl-dev git -y

RUN gem install bundler
# configure plantum dependencies
ADD http://repo1.maven.org/maven2/net/sourceforge/plantuml/plantuml/$PLANTUML_VERSION/plantuml-$PLANTUML_VERSION.jar /tmp/plantuml.jar
RUN echo "#!/bin/bash" > /tmp/plantuml
RUN echo "java -jar /tmp/plantuml.jar \"\$1\" \"\$2\"" >> /tmp/plantuml
RUN mv /tmp/plantuml  /usr/bin/plantuml
RUN chmod u+x /usr/bin/plantuml

WORKDIR /jekyll_content

ENTRYPOINT ["/usr/local/bin/bundle"]
