FROM java:9-jre
LABEL Author="Rafal Sladek rafal.sladek@gmail.com"

ENV TZ=Europe/Berlin
ENV DAEMON_VERSION=0.36.5
ENV DAEMON_FILE=server-${DAEMON_VERSION}-java8.jar
ENV DAEMON_SRC=https://github.com/blynkkk/blynk-server/releases/download/v${DAEMON_VERSION}/${DAEMON_FILE}

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get -yq update && \
    apt-get -y upgrade && \
    apt-get autoclean autoremove -yq && \
    apt-get clean -yq

RUN apt-get -y install tree wget tzdata libxrender1

RUN dpkg-reconfigure -f noninteractive tzdata

RUN cd /root && \
    echo $DAEMON_SRC && \
    wget -q $DAEMON_SRC && \
    tree

WORKDIR /root
VOLUME [ "/root/data" ]
EXPOSE  9443 8080 8441
ADD server.properties .

CMD java -jar ${DAEMON_FILE} -dataFolder /root/data
