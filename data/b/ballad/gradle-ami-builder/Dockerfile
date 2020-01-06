FROM gradle:4.5.1-jdk8

USER root

# Install jfrog client
RUN curl -fL https://getcli.jfrog.io | sh && \
    mv jfrog /usr/local/bin && \
    chmod a+x /usr/local/bin/jfrog

ENV PACKER_VERSION=1.4.5

RUN wget https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip && \
    unzip packer_${PACKER_VERSION}_linux_amd64.zip && \
    mv packer /usr/local/bin && \
    chmod a+x /usr/local/bin/packer


ENV TERRAFORM_VERSION=0.12.13

ADD https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip /tmp/terraform.zip
RUN cd /usr/local/bin \
    && unzip /tmp/terraform.zip \
    && chmod +x /usr/local/bin/terraform \
    && rm /tmp/terraform.zip

USER gradle
