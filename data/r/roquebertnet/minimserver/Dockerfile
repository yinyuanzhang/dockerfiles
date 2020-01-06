FROM java:8-jre

ARG url=http://jminim.com/brac/MinimServer-0.8.5.2-linux-intel.tar.gz

RUN wget -O /opt/MinimServer.tar.gz ${url} && \
		cd /opt && \
		tar xf MinimServer.tar.gz && \
		rm MinimServer.tar.gz

COPY ./minimserver.config /opt/minimserver/data/minimserver.config

EXPOSE 9790/tcp 9791/tcp 1900/udp

# Comment ENTRYPOINT if you would like to launch a shell in the container in interactive mode
ENTRYPOINT [ "/opt/minimserver/bin/startc" ]