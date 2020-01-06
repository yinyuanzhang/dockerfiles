FROM docker:dind

RUN apk add --update \
    bash \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install --upgrade pip \
  && pip install virtualenv \
  && pip install awscli --upgrade \
  && rm -rf /var/cache/apk/*

COPY ./.aws /root/.aws/

ENV PATH $HOME/.local/bin:$PATH
