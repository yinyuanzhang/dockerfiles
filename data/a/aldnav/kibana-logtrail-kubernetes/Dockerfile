FROM docker.elastic.co/kibana/kibana-oss:6.4.0

RUN bin/kibana-plugin install https://github.com/sivasamyk/logtrail/releases/download/v0.1.30/logtrail-6.4.0-0.1.30.zip

COPY logtrail.json /kibana/installedPlugins/logtrail/logtrail.json
