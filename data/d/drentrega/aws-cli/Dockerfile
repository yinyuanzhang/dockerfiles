FROM amazonlinux:2

LABEL vendor="Dr.Entrega" \
      maintainer="Dr.Entrega <technology+docker@drentrega.com>" \
      image="amazonlinux" \
      tag="2"

USER root

ENV PYTHONIOENCODING="UTF-8" \
    PATH="/root/.local/bin:$PATH"

RUN yum update -yq \
  && yum upgrade -yq \
  && yum install -yq aws-cli groff-base \
  && yum clean all -yq \
  && yum autoremove -yq \
  && echo "export PATH=/root/.local/bin:$PATH" >> /root/.bash_profile \
  && aws configure set default.region us-east-1 \
  && aws configure set default.output json

# This dockerfile was auto-generated at 2019-01-10T11:38:34-02:00.

# In case of security branches, please contact technology+security@drentrega.com.