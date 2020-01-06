FROM graylog/graylog:3.1.3

ENV GRAYLOG_SLACK_PLUGIN=3.1.0
ENV GRAYLOG_ALERTMANAGER_PLUGIN=1.2.1

RUN curl -fsL -o /usr/share/graylog/plugin/graylog-plugin-slack-${GRAYLOG_SLACK_PLUGIN}.jar \
      https://github.com/graylog-labs/graylog-plugin-slack/releases/download/${GRAYLOG_SLACK_PLUGIN}/graylog-plugin-slack-${GRAYLOG_SLACK_PLUGIN}.jar

RUN curl -fsL -o /usr/share/graylog/plugin/graylog-plugin-alertmanagercallback-${GRAYLOG_ALERTMANAGER_PLUGIN}.jar \
      https://github.com/GDATASoftwareAG/Graylog-Plugin-AlertManager-Callback/releases/download/1.2.1/graylog-plugin-alertmanagercallback-${GRAYLOG_ALERTMANAGER_PLUGIN}.jar
