FROM docker:18.09

ENV AWSCLI_VERSION "1.16.169"

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
    awscli==$AWSCLI_VERSION
