FROM knobik/consul-agent:release-1.3.0

ADD ./config /config/
ENTRYPOINT ["/bin/consul", "agent", "-server", "-config-dir=/config"]
