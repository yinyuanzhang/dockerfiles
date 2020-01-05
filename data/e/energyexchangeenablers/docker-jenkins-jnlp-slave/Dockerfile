FROM jenkins/jnlp-slave:latest

ARG KUBECTL_VERSION=v1.12.6
ARG HELM_VERSION=v2.6.2
ARG PROMETHEUS_VERSION=1.8.2
ARG DOTNET_RUNTIME_VERSION=2.2
ARG DOTNET_SDK_VERSION=2.2

USER root

RUN apt-get update && apt-get install -y make && apt-get install -y build-essential g++ python-pip jq libyaml-dev libpython2.7-dev libpython-dev python-virtualenv python3 libpython3-dev python3-nose
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates curl wget gnupg gpg --no-install-recommends
RUN pip install awscli

# Add the kubernetes cli
RUN curl -LO https://dl.k8s.io/${KUBECTL_VERSION}/kubernetes-client-linux-amd64.tar.gz \
	&& tar xzf kubernetes-client-linux-amd64.tar.gz \
	&& rm kubernetes-client-linux-amd64.tar.gz \
	&& chmod +x ./kubernetes/client/bin/kubectl \
	&& mv ./kubernetes/client/bin/kubectl /usr/local/bin/kubectl \
	&& rm -Rf ./kubernetes

# Add the helm cli
RUN curl -LO https://kubernetes-helm.storage.googleapis.com/helm-${HELM_VERSION}-linux-amd64.tar.gz \
	&& tar xzf helm-${HELM_VERSION}-linux-amd64.tar.gz \
	&& rm helm-${HELM_VERSION}-linux-amd64.tar.gz \
	&& mv ./linux-amd64/helm /usr/local/bin/helm \
	&& rm -Rf ./linux-amd64

# Add promtool (for verifying prometheus rules)
RUN curl -LO https://github.com/prometheus/prometheus/releases/download/v${PROMETHEUS_VERSION}/prometheus-${PROMETHEUS_VERSION}.linux-amd64.tar.gz \
    && tar xzf prometheus-${PROMETHEUS_VERSION}.linux-amd64.tar.gz \
    && mv ./prometheus-${PROMETHEUS_VERSION}.linux-amd64/promtool /usr/local/bin/promtool \
	&& chmod +x /usr/local/bin/promtool \
    && rm -Rf ./prometheus-${PROMETHEUS_VERSION}.linux-amd64

# Add dotnetcore
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.asc.gpg  \
    && mv microsoft.asc.gpg /etc/apt/trusted.gpg.d/ \
    && wget -q https://packages.microsoft.com/config/debian/9/prod.list \
    && mv prod.list /etc/apt/sources.list.d/microsoft-prod.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends dotnet-runtime-deps-$DOTNET_RUNTIME_VERSION  dotnet-runtime-$DOTNET_RUNTIME_VERSION dotnet-sdk-$DOTNET_SDK_VERSION

# Install deps + add Chrome Stable + purge all the things
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
	&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
	&& apt-get update \
	&& apt-get install -y  google-chrome-stable --no-install-recommends

# Cleanup
RUN apt-get purge --auto-remove -y curl wget gnupg \
	&& rm -rf /var/lib/apt/lists/*