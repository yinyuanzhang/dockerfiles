FROM alpine:3.9.2

RUN apk -v --update add \
	python \
	py-pip \
	groff \
	curl \
	less \
	mailcap \
	docker \
	bash
RUN	pip install --upgrade awscli==1.14.5 && \
	apk -v --purge del py-pip && \
	rm /var/cache/apk/*
RUN	curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
RUN	chmod +x ./kubectl
RUN	mv ./kubectl /usr/local/bin/kubectl

VOLUME /root/.aws
VOLUME /project
WORKDIR /project

CMD ["aws"]
