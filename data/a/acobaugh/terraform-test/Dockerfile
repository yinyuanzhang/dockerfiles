FROM alpine:3.10

ENV TERRAFORM_VERSION=0.12.4
ENV RUBY_VERSION=2.4.6
ENV TERRATEST_LOG_PARSER_VERSION=0.17.5
ENV TERRAFORM_DOCS_VERSION=v0.6.0

ENV TF_TEST_PATH=/terraform-test

# custom bin directory
RUN mkdir -p ${TF_TEST_PATH}
ADD bin ${TF_TEST_PATH}/bin
RUN chmod +x ${TF_TEST_PATH}/bin/*
ENV PATH=${TF_TEST_PATH}/bin:$PATH

# update/upgrade and all other packages
RUN apk update \
 && apk upgrade \
 && apk add curl gnupg go git unzip bash libssl1.1 libcrypto1.1 libffi-dev build-base linux-headers zlib-dev openssl-dev readline-dev

# terraform
ADD pgp_keys.asc .
RUN curl -Os https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
 && curl -Os https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS \
 && cat pgp_keys.asc | gpg --import \
 && curl -Os https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS.sig \
 && gpg --verify terraform_${TERRAFORM_VERSION}_SHA256SUMS.sig terraform_${TERRAFORM_VERSION}_SHA256SUMS \
 && sha256sum -c terraform_${TERRAFORM_VERSION}_SHA256SUMS 2>&1 | grep "${TERRAFORM_VERSION}_linux_amd64.zip:\sOK" \
 && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin \
 && rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip

# terraform-docs
RUN curl -Os https://github.com/segmentio/terraform-docs/releases/download/${TERRAFORM_DOCS_VERSION}/terraform-docs-${TERRAFORM_DOCS_VERSION}-linux-amd64 \
 && mv terraform-docs-${TERRAFORM_DOCS_VERSION}-linux-amd64 /usr/local/bin/terraform-docs

# gopath
ENV GOPATH $HOME/go

# rbenv
ENV PATH /usr/local/rbenv/shims:/usr/local/rbenv/bin:$PATH
ENV RBENV_ROOT /usr/local/rbenv
ENV RUBY_CONFIGURE_OPTS --disable-install-doc

RUN git clone https://github.com/rbenv/rbenv.git /usr/local/rbenv \
 && echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh \
 && mkdir -p "$(rbenv root)"/plugins \
 && git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build

# ruby
RUN rbenv install ${RUBY_VERSION} \
 && rbenv rehash \
 && rbenv global ${RUBY_VERSION}

# bundler
RUN gem update --system && gem install --force bundler

# terratest_log_parser
RUN curl --location --silent --fail --show-error -o terratest_log_parser https://github.com/gruntwork-io/terratest/releases \
 && chmod +x terratest_log_parser \
 && mv terratest_log_parser /usr/local/bin

WORKDIR /work
