FROM alpine:3.6
RUN apk -v --update add \
	ca-certificates \
	openssl \
        python \
        py-pip \
        groff \
	gzip \
	mysql-client \
	postgresql-client \
	zip \
        less \
        mailcap \
	curl \	
        && \
    update-ca-certificates && \
    pip install --upgrade awscli s3cmd python-magic && \
    apk -v --purge del py-pip && \
    rm /var/cache/apk/*
RUN mkdir /data
VOLUME ["/data"]
WORKDIR /data
ENTRYPOINT ["/bin/sh", "-c"]
