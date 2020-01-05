FROM docker.elastic.co/kibana/kibana-oss:6.2.3

RUN bin/kibana-plugin install https://github.com/sivasamyk/logtrail/releases/download/v0.1.27/logtrail-6.2.3-0.1.27.zip && \
    bin/kibana-plugin install https://packages.wazuh.com/wazuhapp/wazuhapp-3.2.1_6.2.3.zip

