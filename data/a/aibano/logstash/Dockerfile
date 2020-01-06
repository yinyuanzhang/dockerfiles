FROM logstash:5.0.2

# Install elasticsearch plugin
RUN gosu logstash /usr/share/logstash/bin/logstash-plugin install logstash-output-elasticsearch

#Install GELF plugin
RUN gosu logstash /usr/share/logstash/bin/logstash-plugin install logstash-input-gelf
