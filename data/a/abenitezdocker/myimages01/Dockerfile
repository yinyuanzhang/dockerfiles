FROM openjdk:8-jre-alpine
COPY app/stt-ms-transEngine-0.0.1-SNAPSHOT.jar /stt-ms-transEngine-0.0.1-SNAPSHOT.jar
# runs application

EXPOSE 7006

RUN mkdir /usr/local/speech
RUN mkdir /usr/local/speech/conf
RUN mkdir /usr/local/speech/cltest01
RUN mkdir /usr/local/speech/logs
RUN mkdir /usr/local/speech/work

COPY conf/speech.properties /usr/local/speech/conf/
COPY conf/core-site.xml /usr/local/speech/cltes01/
COPY conf/hbase-site.xml /usr/local/speech/cltes01/
COPY conf/hdfs-site.xml /usr/local/speech/cltes01/
COPY conf/ffmpeg /usr/local/speech/work/

CMD ["/usr/bin/java", "-Dcn=cltest01", "-DpathConfig=/usr/local/speech", "-DfileConfig=speech.properties", "-DappName=appSpeech", "-jar", "-Dspring.profiles.active=default", "/stt-ms-transEngine-0.0.1-SNAPSHOT.jar"]
