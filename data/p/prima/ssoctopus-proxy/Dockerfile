FROM buzzfeed/sso:v1.2.0

RUN curl -s -L -o ./biscuit-linux_amd64.tgz https://github.com/dcoker/biscuit/releases/download/v0.1.3/biscuit-linux_amd64.tgz && \
	tar xzvf biscuit-linux_amd64.tgz && \
	mv biscuit /usr/bin/biscuit && \
	chmod +x /usr/bin/biscuit && \
	rm biscuit-linux_amd64.tgz && \
	mkdir -p /aws  && \
	apt-get update && \
	apt-get install -y python-pip python-dev && \
	pip install awscli --upgrade && \
	apt-get remove -y curl && \
	rm -rf /var/lib/apt/lists/*

EXPOSE 4180

COPY ./files/entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
