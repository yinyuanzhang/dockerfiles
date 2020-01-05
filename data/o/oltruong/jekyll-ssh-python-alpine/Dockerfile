FROM ruby:2.4.2-alpine

LABEL maintainer oltruong<contact@oltruong.com>

ENV JEKYLL_VERSION  3.6.0
ENV MINIMA_VERSION  2.1.1
ENV ASCIIDOCTOR_VERSION 1.5.6.1
ENV ASCIIDOCTOR_PDF_VERSION 1.5.0.alpha.16

RUN apk add --update bash build-base libffi-dev openssh rsync python3
RUN gem install bundler
RUN gem install jekyll -v $JEKYLL_VERSION
RUN gem install minima -v $MINIMA_VERSION
RUN gem install asciidoctor -v $ASCIIDOCTOR_VERSION
RUN gem install asciidoctor-pdf -v $ASCIIDOCTOR_PDF_VERSION
RUN pip3 install --upgrade pip
RUN pip3 install xlrd pytest