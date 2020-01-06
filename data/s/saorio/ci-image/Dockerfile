FROM python:3-alpine3.8
RUN apk --update --no-cache add bash curl wget make gcc g++
ENV SHELL=/bin/bash
RUN pip install --upgrade pip setuptools awscli
RUN rm -r /root/.cache

RUN mkdir .kube
RUN curl --silent --location "https://github.com/weaveworks/eksctl/releases/download/latest_release/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
RUN mv /tmp/eksctl /usr/local/bin
RUN curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/aws-iam-authenticator
RUN curl -o kubectl https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/kubectl
RUN curl -O -L https://github.com/kubernetes-sigs/kustomize/releases/download/v2.0.3/kustomize_2.0.3_linux_amd64
RUN wget https://storage.googleapis.com/kubernetes-helm/helm-v2.12.3-linux-amd64.tar.gz
RUN tar -zxvf helm-v2.12.3-linux-amd64.tar.gz && mv linux-amd64/helm /usr/local/bin/helm
RUN mv kustomize_*_linux_amd64 kustomize
RUN chmod +x ./aws-iam-authenticator
RUN chmod +x ./kubectl
RUN chmod +x ./kustomize
RUN cp ./aws-iam-authenticator /bin/aws-iam-authenticator && export PATH=$HOME/bin:$PATH
RUN cp ./kubectl /bin/kubectl && export PATH=$HOME/bin:$PATH
RUN cp ./kustomize /bin/kustomize

