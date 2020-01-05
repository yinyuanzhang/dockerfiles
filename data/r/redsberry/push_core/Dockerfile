FROM openjdk:8u201-jdk-alpine3.9

RUN apk add build-base libcap-dev

# install apache common daemon
ADD ./dist/commons-daemon-1.0.15-src.tar.gz /usr/local/src/

WORKDIR /usr/local/src/commons-daemon-1.0.15-src/src/native/unix/
RUN ./configure --with-java=$JAVA_HOME
RUN make

# copy run modules
WORKDIR /redsberry
ADD ./dist/push.tar ./

RUN mkdir ./daemon
RUN mkdir ./daemon/logs
RUN mkdir ./daemon/logs/send
RUN cp /usr/local/src/commons-daemon-1.0.15-src/src/native/unix/jsvc ./daemon/

COPY ./dist/redsPushServerd.sh ./daemon/
COPY ./dist/config/* ./bin/com/eberry/reds/config/

RUN chmod +x ./daemon/redsPushServerd.sh

EXPOSE 4301
EXPOSE 4302
EXPOSE 4303

ENTRYPOINT [ "/redsberry/daemon/redsPushServerd.sh" ]
CMD [ "start" ]

# redsPushServerd.sh 수정
# - Docker로 실행시킬경우 start option에 -nodetach 추가시켜야 함.
