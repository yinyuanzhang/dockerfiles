FROM google/cloud-sdk:266.0.0-alpine

ENV YQ_BIN_VERSION 2.2.0
ENV TERRAFORM_VERSION 0.12.10

VOLUME /data

COPY entrypoint.sh entrypoint.sh
COPY commands.sh /data/commands.sh

RUN adduser -S gkh gkh && \
    apk update && apk add ca-certificates gnupg openssl && \
    rm -rf /var/cache/apk/* && \
    gcloud components install kubectl -q --no-user-output-enabled && \
    gcloud -q components install beta && \
    curl --location --output /usr/local/bin/yq https://github.com/mikefarah/yq/releases/download/${YQ_BIN_VERSION}/yq_linux_amd64 && \
    chmod 755 /usr/local/bin/yq && \
    mkdir -p /data && \
    chown gkh /data && \
    chown gkh /entrypoint.sh && \
    chmod +x /entrypoint.sh && \
    chown gkh /data/commands.sh && \
    chmod +x /data/commands.sh

RUN curl -o terraform.zip https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip &&\ 
    unzip terraform.zip &&\
    mv terraform /usr/bin &&\
    rm terraform.zip

USER gkh


ENTRYPOINT ["/entrypoint.sh"]

