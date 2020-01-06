FROM winworks/ops-base

ENTRYPOINT ["dumb-init", "elb-consul"]

COPY bin /usr/local/bin/
COPY elb-consul /usr/local/elb-consul/

RUN cd /usr/local/elb-consul \
	&& bundle install --deployment
