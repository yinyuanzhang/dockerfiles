FROM giabar/gb-sbt
ENV KFKMANVER=2.0.0.2
ADD https://github.com/yahoo/kafka-manager/archive/$KFKMANVER.tar.gz /
RUN tar zxvf $KFKMANVER.tar.gz &&\
    rm -f $KFKMANVER.tar.gz &&\
    mv kafka-manager-$KFKMANVER kafkamanager
WORKDIR /kafkamanager
RUN sbt clean dist

FROM openjdk:8-jdk-alpine
ENV KFKMANVER=2.0.0.2
COPY --from=0 /kafkamanager/target/universal/kafka-manager-$KFKMANVER.zip .
RUN apk add bash &&\
    unzip kafka-manager-$KFKMANVER.zip &&\
    mv kafka-manager-$KFKMANVER kafka-manager &&\
    rm -f kafka-manager-$KFKMANVER.zip &&\
    mv kafka-manager /
CMD ["/kafka-manager/bin/kafka-manager"]
EXPOSE 9000
