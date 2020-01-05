FROM docker:latest
MAINTAINER ayunyan <ayunyan@gmail.com>

ENV PATH $PATH:/google-cloud-sdk/bin

RUN apk add --no-cache python &&\
    wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz &&\
    tar zxfv google-cloud-sdk.tar.gz &&\
    rm google-cloud-sdk.tar.gz &&\
    /google-cloud-sdk/install.sh --usage-reporting=false &&\
    gcloud components update &&\
    gcloud components install kubectl


