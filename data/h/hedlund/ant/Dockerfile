# Based on: https://registry.hub.docker.com/u/webratio/ant/

FROM hedlund/java:8
MAINTAINER henrik@hedlund.im

ENV ANT_VERSION 1.9.5

# Install Ant
RUN cd && \
	wget -q http://www.us.apache.org/dist//ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz && \
	tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \
	mv apache-ant-${ANT_VERSION} /opt/ant && \
	rm apache-ant-${ANT_VERSION}-bin.tar.gz

# Setup environment
ENV ANT_HOME /opt/ant
ENV PATH ${PATH}:/opt/ant/bin

# Create working directory
RUN mkdir -p /code
VOLUME [ "/code" ]
WORKDIR /code

ENTRYPOINT [ "ant" ]