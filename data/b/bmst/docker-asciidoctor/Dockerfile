FROM ubuntu:19.04

RUN apt-get update -y && \
    apt-get install -y ruby ruby-dev build-essential pkg-config libxml++2.6-dev libxslt1-dev openjdk-8-jre graphviz python2 && \
    echo "gem: --bindir /usr/bin" >> ~/.gemrc && \
    gem install pkg-config && \
    NOKOGIRI_USE_SYSTEM_LIBRARIES=1 gem install asciidoctor-epub3 asciidoctor-pdf --pre && \
    gem install asciidoctor asciidoctor-diagram asciidoctor-plantuml pygments.rb coderay asciidoctor-rouge

ENV GRAPHVIZ_DOT=/usr/bin/dot
