FROM datadog/docker-dd-agent:latest

RUN echo '    collect_labels_as_tags: ["empire.app.name", "empire.app.release", "empire.app.id", "empire.app.process"]' >> /etc/dd-agent/conf.d/docker_daemon.yaml

# Enable per core metrics:
# https://docs.datadoghq.com/integrations/system/#agent-check-system-cores
RUN printf 'init_config:\ninstances:\n  - {}\n' >> /etc/dd-agent/conf.d/system_core.yaml
