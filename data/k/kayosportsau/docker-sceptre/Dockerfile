FROM alpine:3.9


RUN apk update
RUN apk -v --no-cache add \
        python3 \
        ca-certificates \
        groff \
        less \
        bash \
        bash-completion \
        make \
        curl \
        wget \
        zip \
        git \
        vim \
        tree \
        openssl \
        gcc \
        jq \
        musl-dev \
        busybox-extras \
        tmux \
        procps \
        gettext \
        && \
    pip3 install --no-cache-dir --upgrade \
         sceptre>=2.1.3 \
         troposphere>=2.0.0 \
         awscli 


RUN echo "export LC_ALL=C.UTF-8" >> /root/.bashrc
RUN echo "export LANG=C.UTF-8"   >> /root/.bashrc
RUN echo 'export PS1="\u@\h:\w \$ "' >> /root/.bashrc

ADD json2yaml /usr/local/bin/json2yaml
RUN chmod +x /usr/local/bin/json2yaml

RUN curl -o kubectl https://amazon-eks.s3-us-west-2.amazonaws.com/1.12.7/2019-03-27/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mkdir -p /root/bin && cp ./kubectl /root/bin/kubectl && export PATH=/root/bin:$PATH

RUN curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.12.7/2019-03-27/bin/linux/amd64/aws-iam-authenticator
RUN chmod +x ./aws-iam-authenticator
RUN mkdir -p /root/bin && cp ./aws-iam-authenticator /root/bin/aws-iam-authenticator && export PATH=/root/bin:$PATH

RUN echo 'export PATH=/root/bin:$PATH' >> /root/.bashrc

RUN curl -LO https://git.io/get_helm.sh
RUN chmod 700 get_helm.sh
RUN ./get_helm.sh

RUN helm init --client-only
RUN helm plugin install https://github.com/rimusz/helm-tiller
RUN helm plugin install https://github.com/databus23/helm-diff --version master

#RUN wget -O helmfile https://github.com/roboll/helmfile/releases/download/v0.78.0/helmfile_linux_amd64

RUN wget -O helmfile https://github.com/roboll/helmfile/releases/download/v0.80.0/helmfile_linux_amd64
RUN chmod +x ./helmfile
RUN cp ./helmfile /root/bin/helmfile

#Install JX 
ARG JX_VERSION=v2.0.420
RUN mkdir -p ~/.jx/bin
RUN curl -L https://github.com/jenkins-x/jx/releases/download/$JX_VERSION/jx-linux-amd64.tar.gz | tar xzv -C ~/.jx/bin
RUN export PATH=$PATH:/root/.jx/bin
RUN echo 'export PATH=$PATH:/root/.jx/bin' >> /root/.bashrc
RUN echo "source <(kubectl completion bash)" >> /root/.bashrc 
RUN echo "source <(jx completion bash)" >> /root/.bashrc 


#kubetail
RUN wget https://raw.githubusercontent.com/johanhaleby/kubetail/master/kubetail && chmod +x kubetail && mv kubetail /usr/local/bin 

# INSTALL EKSCTL
ARG EKSCTL_VERSION=latest_release
RUN curl --location "https://github.com/weaveworks/eksctl/releases/download/${EKSCTL_VERSION}/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
RUN mv /tmp/eksctl /usr/local/bin


RUN git config --global alias.co checkout
RUN git config --global alias.br branch
RUN git config --global alias.st status

ADD dev-cheats /root/dev-cheats
RUN echo 'export PATH=$PATH:/root/dev-cheats/' >> /root/.bashrc

RUN echo "alias dep='kubectl get deploy'" >> /root/.bashrc
RUN echo "alias ing='kubectl get ing'" >> /root/.bashrc
RUN echo "alias svc='kubectl get svc'" >> /root/.bashrc
RUN echo "alias pods='kubectl get pods'" >> /root/.bashrc
RUN echo "alias k=kubectl" >> /root/.bashrc
RUN echo 'alias ap="kubectl get pods --all-namespaces"' >> /root/.bashrc
RUN echo "alias po='kubectl get pods'" >> /root/.bashrc

WORKDIR /src