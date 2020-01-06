FROM amazonlinux:2
LABEL maintainer="rajesh.jonnalagadda@phenompeople.com" \
	  version="4.0.7"
EXPOSE 27017
ARG MONGODB_VERSION=4.0.7
ARG MONGO_HOME=/opt/mongodb
RUN yum install wget shadow-utils tar gzip -y -q && \
	useradd mongod -u 498  && \
	wget -q -O /tmp/mongodb.tar.gz https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-amazon2-${MONGODB_VERSION}.tgz && \
	tar -xzf /tmp/mongodb.tar.gz -C /opt/ && \
	ln -sf /opt/mongodb-linux-x86_64-amazon2-${MONGODB_VERSION} /opt/mongodb
ADD start-server.sh /opt/mongodb/start-server.sh
RUN mkdir -p /var/log/mongodb /etc/mongodb /var/run/mongodb /var/lib/mongo && \
	touch /var/log/mongodb/mongod.log && \
	chown -R mongod:mongod /var/log/mongodb /var/lib/mongo /var/run/mongodb /opt/mongodb && \	
	chmod a+x /opt/mongodb/start-server.sh
ADD mongod.conf /etc/mongod.conf
ENV MONGO_HOME=${MONGO_HOME} \
	PATH=${MONGO_HOME}/bin:$PATH
USER mongod
ENTRYPOINT ["/opt/mongodb/start-server.sh"]
