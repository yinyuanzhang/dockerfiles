FROM google/cloud-sdk

ARG TERRAFORM_VERSION=0.11.7
ARG MYKE_VERSION=1.0.0

#tools
RUN \
    apt-get update \
    && apt-get -y install gettext-base jq unzip uuid-runtime \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl \
    && chmod +x ./kubectl \
    && mv ./kubectl /usr/local/bin/kubectl 

#helm
RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get >get_helm.sh \
    && chmod 700 get_helm.sh \
    && ./get_helm.sh \
    && helm init --client-only

#myke
RUN curl -LO https://github.com/goeuro/myke/releases/download/v${MYKE_VERSION}/myke_linux_amd64 \
    && chmod +x myke_linux_amd64 \
    && mv myke_linux_amd64 /usr/local/bin/myke \
    && myke --version

#git
RUN git config --global user.email "support@opla.ai" \
    && git config --global user.name "CircleCI"

#terraform
RUN curl -LO https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && mv terraform /usr/local/bin/

#openstack
RUN pip install python-openstackclient

#retry
RUN sh -c "curl https://raw.githubusercontent.com/kadwanev/retry/master/retry -o /usr/local/bin/retry && chmod +x /usr/local/bin/retry"
