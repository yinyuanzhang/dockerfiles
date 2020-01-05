FROM		taig/java

MAINTAINER	Niklas Klein <my.taig@gmail.com>

RUN			wget http://downloads.typesafe.com/play/2.2.3/play-2.2.3.zip && \
            unzip \
                -d opt/ \
                play-2.2.3.zip \
                -x "play-2.2.3/samples/*" && \
            rm play-2.2.3.zip && \
            ln -s /opt/play-2.2.3/play /usr/local/bin/play

EXPOSE		9000 9999
