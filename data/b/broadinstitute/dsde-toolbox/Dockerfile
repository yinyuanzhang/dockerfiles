FROM alpine:3.9

ENV VAULT_VERSION=0.6.5 \
    CONSUL_TEMPLATE_VERSION=0.20.0 \
    CLOUDSDK_PYTHON_SITEPACKAGES=1 \
    VAULT_ADDR='https://clotho.broadinstitute.org:8200'
COPY config.json /etc/consul-template/config/config.json
COPY mysql.json /usr/local/etc/
COPY mytop /usr/bin/mytop
COPY innotop/innotop /usr/local/bin/innotop
COPY innotop/innotop.1 /usr/local/share/man/man1/innotop.1

RUN echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
    echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk update && \
    apk add perl-carp perl-compress-raw-bzip2 \
    perl-compress-raw-zlib  perl-dbd-mysql \
    perl-dbi  perl-data-dumper@community \
    perl-exporter \
    perl-file-temp  perl-getopt-long \
    perl-io-compress perl-pathtools \
    perl-socket perl-term-readkey \
    perl-time-local@community \
    perl-time-hires \
    bash \
    ca-certificates \
    curl \
    findutils \
    jq \
    make \
    nodejs \
    nodejs-npm \
    tzdata \
    ruby ruby-io-console ruby-bundler \
    curl-dev ruby-dev build-base \
    mysql-client \
    openssl \
    python \
    py-pip \
    util-linux \
    vim \
    wget \
    postgresql-client && \
    wget --no-check-certificate https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip -O /tmp/vault_${VAULT_VERSION}_linux_amd64.zip && \
    wget --no-check-certificate https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -O /tmp/consul_template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip -O /tmp/google-cloud-sdk.zip &&\
    cd /tmp && \
    unzip vault_${VAULT_VERSION}_linux_amd64.zip && \
    unzip consul_template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    mv consul-template vault /usr/local/bin/ && \
    cd /usr/local && unzip /tmp/google-cloud-sdk.zip && \
    google-cloud-sdk/install.sh --usage-reporting=false --path-update=true --bash-completion=true && \
    google-cloud-sdk/bin/gcloud config set --installation component_manager/disable_update_check true && \
    rm -rf /tmp/* && \
    rm -rf /var/tmp/* && \
    pip install google-auth google-auth-httplib2 google-api-python-client

COPY binary2string.sh \
     create-token.sh \
     mysql-connect.sh \
     render-templates.sh \
     run-mytop.sh \
     status \
     envStatus \
     run-innotop.sh \
     tokenInfo \
     vault-edit \
     gen-all-tokens.sh \
     configure.rb \
     render-ctmpls.sh \
     jenkins-cleanup.sh \
     /usr/local/bin/
COPY dashboards /usr/local/dashboards

RUN cd /usr/local/dashboards && \
    npm install && \
    chmod 0755 /usr/local/bin/*

COPY Gemfile /usr/app/
RUN cd /usr/app && bundle install && rm -rf /root/.bundle


WORKDIR /working
