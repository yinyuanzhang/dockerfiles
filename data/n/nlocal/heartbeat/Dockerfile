FROM docker.elastic.co/beats/heartbeat:7.4.2
COPY ./config/heartbeat.docker.yml /usr/share/heartbeat/heartbeat.yml
COPY ./config/policy.json /usr/share/heartbeat/policy.json
COPY ./monitors.d/base_monitors.yml /usr/share/heartbeat/monitors.d/base_monitors.yml
USER root
RUN chown root:heartbeat /usr/share/heartbeat/heartbeat.yml
RUN chown root:heartbeat /usr/share/heartbeat/monitors.d/base_monitors.yml
RUN chown root:heartbeat /usr/share/heartbeat/policy.json
USER heartbeat
