FROM alpine:3.4

ENV TERRAFORM_VERSION 0.8.4
ENV GLIBC_VERSION 2.23-r1

RUN apk add --update wget ca-certificates unzip curl && \
    wget -q "https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" && \
    apk add --allow-untrusted glibc-${GLIBC_VERSION}.apk && \
    wget -q -O /terraform.zip "https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip" && \
    unzip /terraform.zip -d /bin && \
    apk del --purge wget ca-certificates unzip && \
    rm -rf /var/cache/apk/* glibc-${GLIBC_VERSION}.apk /terraform.zip

VOLUME ["/terraform"]
WORKDIR /terraform

CMD ["--help"]
