FROM comptel/docker-alpine-base:v36.1

ENV DD_HOME=/opt/datadog-agent
ENV \
    # prevent the agent from being started after install
    DD_START_AGENT=0 \
    DOCKER_DD_AGENT=yes \
    PYCURL_SSL_LIBRARY=openssl \
    AGENT_VERSION=5.25.1 \
    DD_ETC_ROOT="$DD_HOME/agent" \
    PATH="$DD_HOME/venv/bin:$DD_HOME/agent/bin:$PATH" \
    PYTHONPATH="$DD_HOME/agent" \
    DD_CONF_LOG_TO_SYSLOG=no \
    NON_LOCAL_TRAFFIC=yes \
    DD_SUPERVISOR_DELETE_USER=yes \
    DCOS_METRICS_PLUGIN_VERSION="1.11.0-5-gc863f06"

# Add install file
ADD https://raw.githubusercontent.com/DataDog/dd-agent/$AGENT_VERSION/packaging/datadog-agent/source/setup_agent.sh /tmp/setup_agent.sh

# Expose supervisor and DogStatsD port
EXPOSE 9001/tcp 8125/udp

# Install minimal dependencies
RUN apk add -qU --no-cache coreutils curl curl-dev python-dev tar sysstat libintl openssl \
  && apk add -qU --no-cache -t .build-deps gcc musl-dev postgresql-dev linux-headers gettext \
  # Copy envsubst over from gettext
  && cp /usr/bin/envsubst /usr/local/bin/envsubst \
  # Install the agent
  && sh /tmp/setup_agent.sh \
  # Pip for extra packages
  && "${DD_HOME}"/venv/bin/pip install \
    # requests_unixsocket for DCOS node health requests
      requests_unixsocket \
    # 'businesstime' and 'pytz' for bt.py
      businesstime=="0.3.0" \
      pytz=="2018.5" \
  # Clean build dependencies
  && apk del -q .build-deps \
  # Configure the Agent
  # Copy example file and remove network default check
  && cp "$DD_ETC_ROOT/datadog.conf.example" "$DD_ETC_ROOT/datadog.conf" \
  && rm "$DD_ETC_ROOT/conf.d/network.yaml.default" \
  # Remove setup script
  && rm /tmp/setup_agent.sh

COPY files/ /

# URL: https://s3.amazonaws.com/datad0g-process-agent/process-agent-amd64-[VERSION]
ADD https://s3.amazonaws.com/datad0g-process-agent/process-agent-amd64-${AGENT_VERSION} /usr/local/bin/process-agent

RUN chmod +x pre-cmd.sh dcos-metrics-datadog-plugin@"${DCOS_METRICS_PLUGIN_VERSION}" probe.sh /usr/local/bin/process-agent \
    && mv pre-cmd.sh /usr/local/bin/pre-cmd.sh \
    # Override default integrations http_check due to https://github.com/DataDog/integrations-core/issues/1634
    && mv http_check.py /opt/datadog-agent/venv/lib/python2.7/site-packages/datadog_checks/http_check/http_check.py \
    # process-agent.conf is the supervisor conf file for the process-agent program
    && mv process-agent.conf "$DD_ETC_ROOT/process-agent.conf" \
    && mv dcos-metrics-datadog-plugin@"${DCOS_METRICS_PLUGIN_VERSION}" /usr/local/bin/dcos-metrics-datadog \
    # dd-metrics.conf is the supervisor conf part that enables dcos metrics collection via the plugin
    && mv dd-metrics.conf "$DD_ETC_ROOT/dd-metrics.conf" \
    && mv probe.sh "${DD_HOME}/probe.sh" \
    && mv config_builder.py "${DD_HOME}/config_builder.py" 

# Extra conf.d and checks.d
VOLUME ["/conf.d", "/checks.d"]

WORKDIR "$DD_HOME"

# Healthcheck
HEALTHCHECK --interval=5m --timeout=30s --retries=1 \
    CMD ${DD_HOME}/probe.sh

CMD pre-cmd.sh supervisord -c agent/supervisor.conf
