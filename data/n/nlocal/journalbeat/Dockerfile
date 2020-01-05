FROM docker.elastic.co/beats/journalbeat:7.4.2
COPY ./config/journalbeat.docker.yml /usr/share/journalbeat/journalbeat.yml
COPY ./config/policy.json /usr/share/journalbeat/policy.json
USER root
RUN chown root:journalbeat /usr/share/journalbeat/journalbeat.yml
RUN chown root:journalbeat /usr/share/journalbeat/policy.json
USER journalbeat
