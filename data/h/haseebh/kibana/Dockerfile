FROM docker.elastic.co/kibana/kibana-oss:6.6.1
RUN ./bin/kibana-plugin install https://github.com/sivasamyk/logtrail/releases/download/v0.1.31/logtrail-6.6.1-0.1.31.zip
COPY files/logtrail.json /usr/share/kibana/plugins/logtrail/logtrail.json
USER root
COPY cert/* /
USER kibana
