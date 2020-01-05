FROM openjdk:8-jre-alpine

MAINTAINER Shayne Miel <miel.shayne@gmail.com>

RUN apk add --update --no-cache \
	 unzip \
	 wget

ARG CORENLP_RELEASE=stanford-corenlp-full-2018-02-27

RUN wget http://nlp.stanford.edu/software/$CORENLP_RELEASE.zip
RUN unzip $CORENLP_RELEASE.zip && \
	rm $CORENLP_RELEASE.zip

WORKDIR $CORENLP_RELEASE

RUN export CLASSPATH="`find . -name '*.jar'`"

ENV PORT 9000

EXPOSE $PORT

CMD java -cp "*" -mx4g edu.stanford.nlp.pipeline.StanfordCoreNLPServer
