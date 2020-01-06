FROM java:8-alpine

ADD https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-server-0.13.5.jar /elasticmq/elasticmq-server-0.13.5.jar

ADD  elasticmq.conf /elasticmq/elasticmq.conf
ADD  custom.conf /elasticmq/custom.conf
ADD  run /elasticmq/run
RUN  chmod +x /elasticmq/run

EXPOSE 9324

ENTRYPOINT ["/elasticmq/run"]
CMD []
