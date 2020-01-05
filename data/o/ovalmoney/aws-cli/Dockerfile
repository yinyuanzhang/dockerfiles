FROM alpine:3.6

ARG AWSCLI_VERSION="1.16.8"
ARG AWSEBCLI_VERSION="3.14.4"
ARG S3CMD_VERSION="2.0.2"
ARG ECSDEPLOY_VERSION="3.6.0"

RUN apk -v --no-cache add \ 
      bash \
      curl \
      git \
      openssh-client \
      less \
      groff \
      jq \
      python \
      py-pip 

RUN pip install --upgrade --no-cache-dir \
    awscli==$AWSCLI_VERSION \
    awsebcli==$AWSEBCLI_VERSION \
    s3cmd==$S3CMD_VERSION

ADD https://github.com/silinternational/ecs-deploy/archive/${ECSDEPLOY_VERSION}.tar.gz /tmp
RUN tar xf /tmp/${ECSDEPLOY_VERSION}.tar.gz -C /usr/bin/ --strip-components=1 ecs-deploy-${ECSDEPLOY_VERSION}/ecs-deploy && \
    chmod +x /usr/bin/ecs-deploy && \
    rm /tmp/*.tar.gz

VOLUME /root/.aws
VOLUME /project

WORKDIR /project
