FROM alpine:3.5
LABEL maintainer="Devops Israel - <info@devops.co.il"

ENV KUBECTL_VERSION 1.11.1
ENV KOPS_VERSION 1.10.0
ENV HELM_VERSION 2.13.0

#install kubectl
RUN apk add --update \
    curl \
    jq \
    vim \
    tar \
    sed \
    git \
    bash \
    wget \
    bash-doc \
    bash-completion \
    util-linux pciutils usbutils coreutils binutils findutils grep \
    ca-certificates \
    openssh-client \
    && curl -s -L https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl -o /usr/bin/kubectl \
    && chmod +x /usr/bin/kubectl

#install kops
RUN  curl -s -L https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-linux-amd64 -o /usr/bin/kops \
     && chmod +x /usr/bin/kops

RUN curl https://storage.googleapis.com/kubernetes-helm/helm-v${HELM_VERSION}-linux-amd64.tar.gz \
    -o /usr/bin/helm-v${HELM_VERSION}-linux-amd64.tar.gz \
    && tar xvzf /usr/bin/helm-v${HELM_VERSION}-linux-amd64.tar.gz -C /tmp/ \
    && mv /tmp/linux-amd64/helm /usr/bin \
    && chmod +x /usr/bin/helm \
    && helm init --client-only \
    && helm plugin install https://github.com/chartmuseum/helm-push \
    && helm plugin install https://github.com/databus23/helm-diff --version master \
    && helm plugin install https://github.com/adamreese/helm-env \
    && helm plugin install https://github.com/adamreese/helm-last \
    && helm plugin install https://github.com/ContainerSolutions/helm-monitor

#install python and dependencies
RUN apk add --update --no-cache python \
    && python -m ensurepip \
    && rm -r /usr/lib/python*/ensurepip \
    && pip install --upgrade pip setuptools \
    awscli kube-shell --ignore-installed \
    && rm -r /root/.cache

RUN curl -s -L -o /usr/bin/templater https://raw.githubusercontent.com/johanhaleby/bash-templater/master/templater.sh \
    && chmod +x /usr/bin/templater

RUN curl -s -L -o /usr/bin/aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.10.3/2018-07-26/bin/linux/amd64/aws-iam-authenticator \
    && chmod +x /usr/bin/aws-iam-authenticator

RUN curl https://raw.githubusercontent.com/Comcast/k8sh/master/k8sh \
    -o /usr/bin/k8sh \
    && chmod +x /usr/bin/k8sh

WORKDIR /opt
COPY wkops.sh /usr/bin/wkops
COPY eks.sh /usr/bin/eks
COPY bashrc /root/.bashrc

CMD ["bash"]
