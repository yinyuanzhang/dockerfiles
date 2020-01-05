FROM google/cloud-sdk:latest

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# BASICS 
#RUN apk update 
RUN apt-get update 

RUN apt-get install -y  \
      wget \
      #libc6-compat \
      openssh-client \
      ca-certificates  \
      nano

RUN apt-get install -y curl

# NODEJS
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs

#KUBECTL
ENV KUBE_LATEST_VERSION="v1.13.4"
RUN curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
 && chmod +x /usr/local/bin/kubectl \
 #&& apk del --purge deps \
 #&& rm /var/cache/apk/*

#PULUMI CLI
RUN curl -fsSL https://get.pulumi.com | sh
ENV PATH="$PATH:/root/.pulumi/bin"

#HELM CLI
RUN curl https://raw.githubusercontent.com/helm/helm/master/scripts/get | sh
RUN helm init --client-only
