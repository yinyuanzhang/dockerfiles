FROM java:8

ENV CORENLP_ARCHIVE_VERSION=2016-10-31
ENV CORENLP_ARCHIVE=stanford-corenlp-full-${CORENLP_ARCHIVE_VERSION}.zip \
  CORENLP_SHA1SUM=997ae55c34e461e219f8ead9b41eac1a9924af88 \
  CORENLP_PATH=/corenlp \
  CORENLP_SHA1_PATH=corenlp.sha1

RUN wget http://nlp.stanford.edu/software/$CORENLP_ARCHIVE \
  && echo "$CORENLP_SHA1SUM $CORENLP_ARCHIVE" > corenlp.sha1 \
  && sha1sum -c corenlp.sha1 \
  && unzip $CORENLP_ARCHIVE \
  && mv $(basename ../$CORENLP_ARCHIVE .zip) $CORENLP_PATH \
  && rm $CORENLP_ARCHIVE \
  && rm corenlp.sha1
 
RUN wget http://nlp.stanford.edu/software/stanford-english-corenlp-models-current.jar \
  && mv stanford-english-corenlp-models-current.jar $CORENLP_PATH

WORKDIR $CORENLP_PATH

EXPOSE 9000
CMD ["java", "-mx4g", "-cp", "*", "edu.stanford.nlp.pipeline.StanfordCoreNLPServer", "9000"]
