FROM debian:stable-slim

RUN  apt-get -y update && apt-get install -y --no-install-recommends \
	motion \
	&& apt-get clean && apt-get autoremove && rm -rf /var/lib/apt/lists/* && \
    sed -i '/^stream_localhost/ s/on/off/' /etc/motion/motion.conf

EXPOSE 8081

ENTRYPOINT ["/bin/bash", "-c"]

CMD [ "/usr/bin/motion" ]