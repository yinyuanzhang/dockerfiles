FROM devth/helm:v2.14.1

ENV TERRAFORM_VERSION=0.12.5

MAINTAINER USU Software AG

RUN apk --update add jq tzdata zip coreutils gnupg bash-completion && rm -rf /var/cache/apk/*
RUN cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime && echo "Europe/Berlin" >  /etc/timezone

RUN echo ". /etc/profile.d/bash_completion.sh" >> ~/.bashrc 
RUN echo "source <(kubectl completion bash)" >> ~/.bashrc

ADD ./jitcrypt /bin
RUN chmod u+x /bin/jitcrypt

RUN helm plugin install https://github.com/chartmuseum/helm-push

RUN wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
  unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin && \
  rm -f  terraform_${TERRAFORM_VERSION}_linux_amd64.zip
