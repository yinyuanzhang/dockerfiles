FROM openjdk:8
ARG v=1.5.1
ENV PATH $PATH:/play
ENV ANT_HOME /ant
ENV PATH $PATH:$ANT_HOME/bin
RUN curl https://downloads.typesafe.com/play/$v/play-$v.zip --output play.zip \
    && unzip play.zip \
    && rm play.zip \
    && mv play-$v play \
    && chmod a+x /play/play \
    && play version \
    && curl http://mirror.linux-ia64.org/apache//ant/binaries/apache-ant-1.10.5-bin.zip --output ant.zip \
    && unzip ant.zip \
    && rm ant.zip \
    && mv apache-ant-1.10.5 ant \
    && ant -version
