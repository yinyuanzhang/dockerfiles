FROM alpine:3.9
MAINTAINER Brian Macauley <brian.macauley@rewardinsight.com>

ENV EKSTOOLS_VERSION=v0.2
ENV AWSCLI_VERSION=1.16.130
ENV KUBECTL_VERSION=v1.13.4
ENV STERN_VERSION=1.10.0
ENV ISTIOCTL_VERSION=1.1.0
ENV EKSCTL_VERSION=0.1.24
ENV AWS_IAM_AUTHENTICATOR_VERSION=1.11.5/2018-12-06
ENV HELM_VERSION=v2.13.1
ENV KUBECTX_VERSION=0.6.3
ENV STERN_VERSION=1.10.0
ENV KUBETAIL_VERSION=1.6.7
# ENV KAIL_VERSION=0.7.0
ENV KUBESHELL_VERSION=0.0.23
ENV KUBEPS1_VERSION=0.7.0
ENV DRONECLI_VERSION=1.0.7




# update os
RUN apk update

# add utils
RUN apk add  vim curl unzip jq wget less python3 tar gzip bash git

# add prompt, kubectl_aliases
COPY ./files/.bashrc /root/.bashrc
COPY ./files/.kubectl_aliases /root/.kubectl_aliases


#----------------------------
# AWS CLI
#----------------------------

# setup  pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3 get-pip.py

# setup the aws cli (latest at time of docker build)
RUN pip install awscli==${AWSCLI_VERSION} --upgrade


#----------------------------
# kubectl
#----------------------------

# setup kubectl (latest at time of docker build)
# RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin/kubectl


#----------------------------
# eksctl
#----------------------------
RUN curl -L https://github.com/weaveworks/eksctl/releases/download/${EKSCTL_VERSION}/eksctl_Linux_amd64.tar.gz | tar zxv  -C /tmp && \
	mv /tmp/eksctl /usr/local/bin/eksctl && \
	rm -rf /tmp/eksctl && \
	chmod +x /usr/local/bin/eksctl


#----------------------------
# istioctl
#----------------------------
RUN curl -L https://github.com/istio/istio/releases/download/1.1.0/istio-${ISTIOCTL_VERSION}-linux.tar.gz | tar zxv  -C /tmp && \
	mv /tmp/istio-${ISTIOCTL_VERSION}/bin/istioctl /usr/local/bin/istioctl && \
	rm -rf /tmp/istio-${ISTIOCTL_VERSION} && \
	chmod +x /usr/local/bin/istioctl




#----------------------------
# kubernetes utils
#----------------------------

# kns - k8s namespace switcher
# https://github.com/blendle/kns
RUN apk add fzf
RUN curl -LO https://raw.githubusercontent.com/blendle/kns/master/bin/kns && \
	chmod +x ./kns && \
	mv ./kns /usr/local/bin/kns

# ktx - k8s context(cluster) switcher
# https://github.com/blendle/kns
RUN curl -LO https://raw.githubusercontent.com/blendle/kns/master/bin/ktx && \
	chmod +x ./ktx && \
	mv ./ktx /usr/local/bin/ktx


# kubectx & kubens - context switcher and namespace switcher
# https://github.com/ahmetb/kubectx
RUN apk add ncurses
RUN curl -L https://github.com/ahmetb/kubectx/archive/v${KUBECTX_VERSION}.tar.gz | tar zxv  -C /tmp && \
	mv /tmp/kubectx-${KUBECTX_VERSION}/kubectx /usr/local/bin/kubectx && \
	mv /tmp/kubectx-${KUBECTX_VERSION}/kubens /usr/local/bin/kubens && \
	rm -rf /tmp/kubectx-${KUBECTX_VERSION} && \
	chmod +x /usr/local/bin/kubectx && \
	chmod +x /usr/local/bin/kubens

# stern - multi-pod logging
# https://github.com/wercker/stern
RUN curl -LO https://github.com/wercker/stern/releases/download/1.10.0/stern_linux_amd64  && \
	mv ./stern_linux_amd64 /usr/local/bin/stern && \
	chmod +x /usr/local/bin/stern


# kubetail - multi-pod logging
# https://github.com/johanhaleby/kubetail
RUN curl -L https://github.com/johanhaleby/kubetail/archive/${KUBETAIL_VERSION}.tar.gz | tar zxv -C /tmp && \
	mv /tmp/kubetail-${KUBETAIL_VERSION}/kubetail /usr/local/bin/kubetail && \
	rm -rf /tmp/kubetail-${KUBETAIL_VERSION} && \
	chmod +x /usr/local/bin/kubetail


# # kail - multi-pod logging
# # https://github.com/boz/kail
# RUN curl -L https://github.com/boz/kail/releases/download/v${KAIL_VERSION}/kail_${KAIL_VERSION}_linux_amd64.tar.gz | tar zxv -C /tmp && \
# 	mv /tmp/kail /usr/local/bin/kail && \
# 	chmod +x /usr/local/bin/kail


# kube-shell
# https://github.com/cloudnativelabs/kube-shell
RUN pip install kube-shell==${KUBESHELL_VERSION} --upgrade


# kube-ps1
# https://github.com/jonmosco/kube-ps1
RUN curl -L https://github.com/jonmosco/kube-ps1/archive/v${KUBEPS1_VERSION}.tar.gz | tar zxv -C /tmp && \
	mv /tmp/kube-ps1-${KUBEPS1_VERSION}/kube-ps1.sh /root/kube-ps1.sh && \
	chmod +x /root/kube-ps1.sh




#----------------------------
# AWS IAM authenticator
#----------------------------


# setup the IAM authenticator for aws (for Amazon EKS)
RUN curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/${AWS_IAM_AUTHENTICATOR_VERSION}/bin/linux/amd64/aws-iam-authenticator
RUN chmod +x ./aws-iam-authenticator
RUN mv ./aws-iam-authenticator /usr/local/bin

#----------------------------
# Helm
#----------------------------

# setup Helm
RUN curl -L http://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz | tar zxv -C /tmp \
    && mv /tmp/linux-amd64/helm /usr/local/bin/helm \
    && rm -rf /tmp/linux-amd64 \
    && chmod +x /usr/local/bin/helm

# install helm plugins
RUN helm init --client-only

RUN helm plugin install https://github.com/databus23/helm-diff
RUN helm plugin install --version master https://github.com/sagansystems/helm-github.git
RUN helm plugin install https://github.com/IBM/helm-stop
RUN helm plugin install https://github.com/mstrzele/helm-edit
RUN helm plugin install https://github.com/adamreese/helm-env
RUN helm plugin install https://github.com/maorfr/helm-logs
RUN helm plugin install https://github.com/rimusz/helm-tiller
RUN helm plugin install https://github.com/maorfr/helm-backup
RUN helm plugin install https://github.com/hypnoglow/helm-s3.git

RUN helm plugin install https://github.com/rewardinsight/helm-ssm

COPY ./files/motd.sh motd.sh
RUN chmod +x ./motd.sh && ./motd.sh > /etc/motd && rm -f ./motd.sh
RUN echo '[ ! -z "$TERM" -a -r /etc/motd ]  && cat /etc/motd' \
    >> /root/.bashrc

RUN curl -L https://github.com/drone/drone-cli/releases/download/v1.0.7/drone_linux_amd64.tar.gz | tar zx
RUN install -t /usr/local/bin drone

#----------------------------
# Postgres Python script support
#----------------------------
RUN echo Installing dependices...
RUN pip3 install boto3
RUN apk add postgresql-dev
RUN apk add gcc
RUN apk add python3-dev
RUN apk --no-cache add musl-dev
RUN pip3 install psycopg2-binary
