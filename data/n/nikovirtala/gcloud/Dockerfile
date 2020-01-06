FROM python:2.7-alpine
LABEL maintainer "Niko Virtala <niko@nikovirtala.io>"

RUN apk add --no-cache --virtual .build-dependencies \
  ca-certificates curl tar openssh-client git \
  && cd /usr/local \
  && curl -sSLO https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz \
  && tar -zxvf google-cloud-sdk.tar.gz \
  && rm -f google-cloud-sdk.tar.gz \
  && ( \
    cd google-cloud-sdk \
    && ./install.sh \
    --usage-reporting false \
    --path-update true \
  ) \
  && apk del .build-dependencies

RUN adduser -D -g '' -h /home/nikovirtala nikovirtala
USER nikovirtala
WORKDIR /home/nikovirtala
ENV PATH $PATH:/usr/local/google-cloud-sdk/bin

ENTRYPOINT ["gcloud"]
