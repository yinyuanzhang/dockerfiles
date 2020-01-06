FROM docker:stable

LABEL maintainer="alex.khaerov@chainstack.com"
LABEL vendor="Chainstack"

ENV HELM_VERSION="v2.14.1"
ENV CLOUD_SDK="250.0.0"

ENV PATH /usr/lib/google-cloud-sdk/bin/:$PATH

RUN apk add --no-cache \
		python \
		python-dev \
                openssl-dev \
                libffi-dev \
		py-pip \
		git \
		build-base \
		openssh-client \
		ca-certificates \
		bash \
		curl \
		jq \
    && pip install -U pip && pip install dump-env docker-compose \
    && wget -O - https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK}-linux-x86_64.tar.gz \
    | tar xvz -C /usr/lib \
    && bash /usr/lib/google-cloud-sdk/install.sh --additional-components kubectl \
    && wget -q http://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm \
    && chmod +x /usr/local/bin/helm && helm init --service-account ci-helm --client-only \
    && helm plugin install https://github.com/nouney/helm-gcs
