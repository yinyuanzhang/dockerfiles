FROM debian:latest

RUN apt-get update &&  \
    apt-get install -y ca-certificates \
      curl \
      unzip \
      libwww-perl \
      libdatetime-perl && \
    rm -rf /var/lib/apt/lists/*

RUN curl -O https://aws-cloudwatch.s3.amazonaws.com/downloads/CloudWatchMonitoringScripts-1.2.2.zip && \
    unzip CloudWatchMonitoringScripts-1.2.2.zip -d/usr && \
    rm CloudWatchMonitoringScripts-1.2.2.zip

COPY put_metrics.sh /usr/aws-scripts-mon

ENTRYPOINT ["/usr/aws-scripts-mon/put_metrics.sh"]
