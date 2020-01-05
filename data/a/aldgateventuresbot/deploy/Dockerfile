FROM ubuntu:18.04

ENV CLOUD_SDK_VERSION=243.0.0

ADD https://storage.googleapis.com/kubernetes-release/release/v1.13.2/bin/linux/amd64/kubectl /usr/local/bin/kubectl
ADD https://get.helm.sh/helm-v3.0.0-beta.3-linux-amd64.tar.gz /tmp/helm.tar.gz
ADD https://raw.githubusercontent.com/fsaintjacques/semver-tool/master/src/semver /usr/local/bin/semver
ADD https://download.docker.com/linux/static/stable/x86_64/docker-18.09.0.tgz /tmp/docker.tgz
ADD https://github.com/docker/compose/releases/download/1.23.1/docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
ADD https://raw.githubusercontent.com/rockymadden/slack-cli/master/src/slack /usr/local/bin/slack
ADD https://github.com/github/hub/releases/download/v2.12.3/hub-linux-amd64-2.12.3.tgz /tmp/hub.tgz

RUN apt-get update && \
	apt-get install -y curl git ca-certificates lsb-release gnupg jq httpie zip && \
	export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
	echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" > /etc/apt/sources.list.d/google-cloud-sdk.list && \
	curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
	apt-get update && \
	apt-get install -y google-cloud-sdk=${CLOUD_SDK_VERSION}-0 && \
	tar -zxvf /tmp/docker.tgz --strip-components 1 --directory /usr/local/bin/ && \
	tar -zxvf /tmp/hub.tgz && \
	mv hub-*/bin/hub /usr/local/bin && \
	rm -rf hub-* && \
	tar -zxvf /tmp/helm.tar.gz && \
	mv linux-amd64/helm /usr/local/bin/ && \
	rm -rf linux-amd64 && \
	chmod +x /usr/local/bin/docker-compose /usr/local/bin/kubectl /usr/local/bin/helm /usr/local/bin/semver /usr/local/bin/slack && \
	rm -rf /var/lib/apt/lists/* /tmp/* && \
	gcloud --version && \
	kubectl version --client && \
	helm version && \
	docker --version && \
	docker-compose --version
