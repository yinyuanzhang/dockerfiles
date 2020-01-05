FROM osxcc/osxcc:latest
MAINTAINER fayazg

ENV TERRAFORM_VERSION=0.11.3

RUN apt-get update -y \
&& apt-get upgrade -y \
&& apt-get install jq curl wget git ca-certificates unzip -y \
&& apt-get clean -y \
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl -o terraform.zip https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
RUN unzip terraform.zip
RUN mv terraform /usr/local/bin/
RUN rm -f terraform*
