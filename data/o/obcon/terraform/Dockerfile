FROM obcon/aws-cli:1.11.64

USER root

ENV GLIBC 2.23-r3
ENV TERRAFORM_VERSION 0.9.5

RUN curl -L https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub -o /etc/apk/keys/sgerrand.rsa.pub && \
    curl -L https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC}/glibc-${GLIBC}.apk -o glibc-${GLIBC}.apk && \
    apk add glibc-${GLIBC}.apk && \
    rm glibc-${GLIBC}.apk

RUN cd /usr/local/bin && \
    curl https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -o terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
    rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip

RUN rm -rf /var/cache/apk/*

USER obcon
