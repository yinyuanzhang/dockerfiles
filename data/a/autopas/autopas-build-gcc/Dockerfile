FROM autopas/build-base:latest

# install openmpi requirements
RUN true \
	&& apt-get -qq update \
	&& apt-get -qq install -y --no-install-recommends \
		libopenmpi-dev \
		openmpi-bin \
	&& rm -rf /var/lib/apt/lists/*

RUN rm /usr/bin/mpirun
RUN echo '/etc/alternatives/mpirun --oversubscribe --allow-run-as-root $@' > /usr/bin/mpirun
RUN chmod +x /usr/bin/mpirun
ENTRYPOINT []

CMD ["sh", "-c", "cmake -GNinja ../.. && ninja && ninja test"]
