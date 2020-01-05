FROM ubuntu:14.04

RUN apt-get update && \
	apt-get install -y curl

RUN echo "deb http://debian.datastax.com/community stable main" | sudo tee -a /etc/apt/sources.list.d/datastax.community.list && \
	curl -L http://debian.datastax.com/debian/repo_key | sudo apt-key add - && \
	apt-get update && \
	apt-get install -y opscenter

EXPOSE 8888
EXPOSE 50031
EXPOSE 61620
