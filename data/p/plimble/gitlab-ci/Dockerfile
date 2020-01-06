FROM golang:1.10-alpine

RUN apk add --no-cache tar gzip curl git openssh-client bash g++

ENV DOCKER_CHANNEL edge
ENV DOCKER_VERSION 17.04.0-ce
ENV KOPS_VERSION 1.9.0
ENV KUBECTL_VERSION v1.10.3
ENV RANCHER_CLI_VERSION v2.0.4
ENV HELM_VERSION v2.9.1
ENV DRAFT_VERSION v0.15.0

RUN set -x \
	&& curl -fSL "https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz" -o helm.tar.gz \
	&& tar -xzvf helm.tar.gz \
	&& mv linux-amd64/helm /usr/local/bin/helm \
	&& rm -rf linux-amd64 helm.tar.gz \
	&& helm version -c \
	&& curl -fSL "https://azuredraft.blob.core.windows.net/draft/draft-${DRAFT_VERSION}-linux-amd64.tar.gz" -o draft.tar.gz \
	&& tar -xzvf draft.tar.gz \
	&& mv linux-amd64/draft /usr/local/bin/draft \
	&& rm -rf linux-amd64 draft.tar.gz \
	&& draft version \
	&& curl -fSL "https://releases.rancher.com/cli/${RANCHER_CLI_VERSION}/rancher-linux-amd64-${RANCHER_CLI_VERSION}.tar.gz" -o rancher.tar.gz \
	&& tar -xzvf rancher.tar.gz \
	&& mv rancher-${RANCHER_CLI_VERSION}/rancher /usr/local/bin/rancher \
	&& rm -rf rancher-${RANCHER_CLI_VERSION} rancher.tar.gz \
	&& rancher -v \
	&& curl -fL "https://download.docker.com/linux/static/${DOCKER_CHANNEL}/x86_64/docker-${DOCKER_VERSION}.tgz" -o docker.tgz \
	&& tar -xzvf docker.tgz \
	&& mv docker/* /usr/local/bin/ \
	&& rmdir docker \
	&& rm docker.tgz \
	&& docker -v \
	&& curl https://glide.sh/get | sh \
	&& curl -LO https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl \
	&& mv kubectl /usr/local/bin/ \
	&& chmod +x /usr/local/bin/kubectl \
	&& curl -fSL https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-linux-amd64 -o kops \
	&& mv kops /usr/local/bin/ \
	&& chmod +x /usr/local/bin/kops \
	&& go get -u github.com/jteeuwen/go-bindata/... \
	&& curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh \
	&& mkdir -p ~/.ssh \
  && chmod 700 ~/.ssh \
  && ssh-keyscan gitlab.com >> ~/.ssh/known_hosts \
  && ssh-keyscan github.com >> ~/.ssh/known_hosts \
  && ssh-keyscan bitbucket.org >> ~/.ssh/known_hosts \
	&& chmod 644 ~/.ssh/known_hosts \
	&& git config --global url."git@github.com:".insteadOf "https://github.com/" \
  && git config --global url."git@gitlab.com:".insteadOf "https://gitlab.com/" \
  && git config --global url."git@bitbucket.org:".insteadOf "https://bitbucket.org/"

COPY docker-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["bash"]
