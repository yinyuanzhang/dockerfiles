FROM google/cloud-sdk:237.0.0-alpine

# Install Docker and GCR Credentials helper
ENV DOCKER_VERSION='18.09.3' \
	DOCKER_API_VERSION='1.23'

RUN apk --no-cache add \
		make \
		jq \
	&& gcloud components install \
		gsutil \
		kubectl \
	&& curl -fsSLO \
		"https://download-stage.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz" \
	&& tar --strip-components=1 -xvzf docker-${DOCKER_VERSION}.tgz -C /usr/local/bin \
	&& rm docker-${DOCKER_VERSION}.tgz \
	&& chmod +x /usr/local/bin/docker

COPY .docker /root/.docker

# Install yamllint
ENV YAMLLINT_VERSION='1.15.0'
RUN apk --no-cache add py-pip \
	&& pip install -q --no-cache-dir "yamllint==${YAMLLINT_VERSION}" \
	&& apk del py-pip

# Install sops
ENV SOPS_VERSION='3.2.0'

RUN curl -sL \
		"https://github.com/mozilla/sops/releases/download/${SOPS_VERSION}/sops-${SOPS_VERSION}.linux" \
		-o /tmp/sops \
	&& chmod +x /tmp/sops \
	&& mv /tmp/sops /usr/local/bin/

# Install Helm and the GCS plugin for chart repos
ENV HELM_VERSION='2.13.0' \
	HELM_GCS_VERSION='0.2.0' \
	HELM_HOME='/root/.helm'

RUN curl -fsSLO \
		"https://storage.googleapis.com/kubernetes-helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz" \
	&& tar --strip-components=1 -xvzf helm-v${HELM_VERSION}-linux-amd64.tar.gz -C /usr/local/bin \
	&& rm helm-v${HELM_VERSION}-linux-amd64.tar.gz \
	&& chmod +x /usr/local/bin/helm \
	&& mkdir -p /root/.helm/plugins \
	&& helm plugin install https://github.com/viglesiasce/helm-gcs.git \
		--version "v${HELM_GCS_VERSION}" \
	&& helm plugin install https://github.com/pagerinc/helm-diff \
		--version 'master'
