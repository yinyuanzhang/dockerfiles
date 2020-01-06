FROM docker:latest

RUN \
	mkdir -p /aws && \
	apk -Uuv add --no-cache groff less python py-pip docker openrc mysql-client && \
	pip install --upgrade pip && \
	pip install awscli && \ 
	pip install boto3 && \
	rm /var/cache/apk/*

