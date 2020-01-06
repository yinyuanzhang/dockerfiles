FROM openjdk:8u212-jre-alpine 

ADD http://nilhcem.github.com/FakeSMTP/downloads/fakeSMTP-latest.zip /fakeSMTP-latest.zip

RUN unzip /fakeSMTP-latest.zip \
    && rm /fakeSMTP-latest.zip \
    && mkdir -p /output

EXPOSE 25

ENTRYPOINT ["java","-jar","/fakeSMTP-2.0.jar","--background", "--output-dir", "/output", "--port", "25", "--start-server"]