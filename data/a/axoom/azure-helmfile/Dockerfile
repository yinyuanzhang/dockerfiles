FROM python:3.7-slim-stretch

RUN apt-get update && apt-get install -y --no-install-recommends 0install-core curl

# Install azure cli
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

# Drop root rights
RUN useradd -m user
USER user
WORKDIR /home/user
ENV PATH="/home/user/bin:${PATH}"

# kubectl
RUN 0install add kubectl http://repo.roscidus.com/kubernetes/kubectl

# Install helm-autoversion
RUN 0install add helm --version 0.3 http://assets.axoom.cloud/tools/helm-autoversion.xml
RUN helm init --client-only

# Install helmfile
RUN curl --silent --fail --location https://github.com/roboll/helmfile/releases/download/v0.80.2/helmfile_linux_amd64 -o bin/helmfile \
 && chmod +x bin/helmfile

# Install sscript
COPY *.sh /
ENTRYPOINT ["/entrypoint.sh"]
