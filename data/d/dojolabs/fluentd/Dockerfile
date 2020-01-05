FROM gcr.io/google-containers/fluentd-elasticsearch:v2.4.0
RUN fluent-gem install fluent-plugin-kafka:0.12.1 fluent-plugin-mqtt-io:0.4.2 fluent-plugin-mutate_filter:1.0.7
#RUN apk add --no-cache logrotate
RUN apt-get update && apt-get install -y cron logrotate
COPY logrotate.conf /etc/logrotate.conf
