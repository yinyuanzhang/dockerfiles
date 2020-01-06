FROM alpine:latest
RUN apk add --no-cache openjdk8-jre
ENV JAVA_HOME=/usr
ENV PATH=$PATH:$JAVA_HOME
RUN apk add --no-cache wget && \
    cd /home && \
	wget "http://apache.40b.nl/nifi/1.8.0/nifi-1.8.0-bin.tar.gz" && tar -xzf nifi-1.8.0-bin.tar.gz -C /home/ && \
    rm /home/nifi-1.8.0-bin.tar.gz && \
	apk del wget
EXPOSE 8080
ENTRYPOINT ["sh","/home/nifi-1.8.0/bin/nifi.sh","run"]
CMD ["/bin/sh"]
