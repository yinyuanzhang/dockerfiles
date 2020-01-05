FROM python:3.4.3

MAINTAINER Patrick H. McJury <patrick.mcjury@macmillan.com>

LABEL Description="Image with aws cli installed"

RUN apt-get update && apt-get install -y \
		curl \
		git \
		less \
		zip \
		groff \
		jq \
		&& rm -r /var/lib/apt/lists/*

RUN pip install awscli

VOLUME /root/.aws

VOLUME /root/data

WORKDIR /root/data

COPY docker-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["docker-entrypoint.sh"] 

CMD ["aws list"]
