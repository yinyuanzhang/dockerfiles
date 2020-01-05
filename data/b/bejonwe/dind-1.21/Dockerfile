FROM jpetazzo/dind

RUN apt-get purge -y docker-engine && \
	apt-get install -y docker-engine=1.9.1-0~trusty

RUN curl -s -L https://github.com/docker/compose/releases/1.7.0 | \
    egrep -o '/docker/compose/releases/download/[0-9.]*/docker-compose-Linux-x86_64' | \
    wget --base=http://github.com/ -i - -O /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose && \
    /usr/local/bin/docker-compose --version

ENV LOG=file
ENTRYPOINT ["wrapdocker"]
CMD []