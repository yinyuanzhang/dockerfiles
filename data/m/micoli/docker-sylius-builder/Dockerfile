FROM micoli/docker-sylius-php:latest

ARG KUBERNETES_VERSION=v1.8.0
ARG HELM_VERSION=v2.10.0

RUN	apk update ;\
	apk add --no-cache --update \
		ca-certificates \
		curl  \
		docker \
		git \
		openssl \
		openssh-client \
		nodejs  \
		nodejs-npm  \
		py-pip \
		sudo \
		bash \
		yarn; \
	\
	pip install docker-compose;\
	\
	curl -L -o /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/${KUBERNETES_VERSION}/bin/linux/amd64/kubectl ; \
	chmod a+x /usr/local/bin/kubectl;\
	\
	curl -o /tmp/helm.tgz https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz  ; \
	tar xvfz /tmp/helm.tgz -C /usr/local/bin/ --strip-components=1 linux-amd64/helm ;\
	chmod a+x /usr/local/bin/helm;\
	\
	apk add go; \
	go get  github.com/VirtusLab/render; \
	go build  github.com/VirtusLab/render; \
	apk del go; \
	sudo mv render /usr/local/bin/render

ENTRYPOINT ["/bin/bash"]

### install gitlab ;\
#echo "Download and install gitlab-runner" ;\
#curl --silent  https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64 -o /usr/local/bin/gitlab-runner ;\
#chmod +x /usr/local/bin/gitlab-runner;\
#\
#RUN echo "annexe" ;\
#	### install gitlab ;\
#	#wget  https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64 -O /usr/local/bin/gitlab-runner ;\
#	#chmod +x /usr/local/bin/gitlab-runner ;\
#	### install docker-compose ;\
#	wget  https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -O /usr/local/bin/docker-compose 2>/dev/null ;\
#	chmod +x /usr/local/bin/docker-compose ;
