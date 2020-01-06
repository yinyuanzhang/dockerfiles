# https://circleci.com/docs/2.0/circleci-images/
FROM circleci/ruby:2.6

USER root

RUN echo "deb https://packages.cloud.google.com/apt cloud-sdk-stretch main" > /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get install -y apt-transport-https && \
    apt-get update -y && \
    apt-get install -y google-cloud-sdk kubectl && \
    apt-get clean && \
    apt-get autoclean && \
    apt-get autoremove && \
    gcloud config set core/disable_usage_reporting true && \
    gcloud config set component_manager/disable_update_check true && \
    curl -sSL https://github.com/shyiko/kubesec/releases/download/0.9.2/kubesec-0.9.2-linux-amd64 -o /usr/local/bin/kubesec && \
    curl -sSL https://github.com/shyiko/kubesec/releases/download/0.9.2/kubesec-0.9.2-linux-amd64.asc -o kubesec.asc && \
    curl -sS https://keybase.io/shyiko/pgp_keys.asc | gpg --import && \
    gpg --verify kubesec.asc /usr/local/bin/kubesec && \
    chmod a+x /usr/local/bin/kubesec && \
    gcloud --version && \
    docker --version && \
    kubectl version --client

USER circleci

RUN gem install brakeman rubocop rubocop-performance rubocop-rails vidar --no-document


