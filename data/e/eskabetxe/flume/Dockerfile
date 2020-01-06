FROM eskabetxe/java
MAINTAINER eskabetxe

ENV FLUME_VERSION=1.8.0
ENV FLUME_PATH=/opt/flume

ENV PATH $FLUME_PATH/bin:$PATH

RUN install_packages wget

RUN mkdir $FLUME_PATH \
    && wget -qO- http://archive.apache.org/dist/flume/$FLUME_VERSION/apache-flume-$FLUME_VERSION-bin.tar.gz \
          | tar zxvf - -C $FLUME_PATH --strip 1

ADD start-flume.sh $FLUME_PATH/bin/start-flume
RUN chmod a+x $FLUME_PATH/bin/start-flume

RUN groupadd flume && \
    useradd -g flume -b $FLUME_PATH flume && \
    chown -R flume:flume $FLUME_PATH && \
    chown -h flume:flume $FLUME_PATH

USER flume
WORKDIR $FLUME_PATH

CMD ["/bin/sh", "-c", "bin/start-flume"]
