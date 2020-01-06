FROM debian:jessie

RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/mms-agent
WORKDIR /opt/mms-agent

RUN curl -sL https://mms.mongodb.com/download/agent/monitoring/mongodb-mms-monitoring-agent-latest.linux_x86_64.tar.gz | \
    tar xz --strip-components=1

CMD ./mongodb-mms-monitoring-agent

ONBUILD COPY monitoring-agent.config /opt/mms-agent/monitoring-agent.config
