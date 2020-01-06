FROM google/cloud-sdk:latest

RUN curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash && \
       helm init --client-only && \
       helm plugin install https://github.com/nouney/helm-gcs

RUN curl -L https://github.com/Praqma/helmsman/releases/download/v1.5.0/Helmsman_1.5.0_linux_amd64.tar.gz | tar zx && \
       mv helmsman /usr/local/bin/helmsman

RUN pip install --no-cache-dir easygoogle \
      ruamel.yaml \
      google-cloud-logging \
      google-cloud-monitoring \
      google-cloud-error-reporting \
      google-cloud-storage \
      google-cloud-datastore \
      google-cloud-bigquery \
      google-cloud-pubsub \
      google-cloud-tasks \
      PyYAML \
      arrow && \
      python -m easygoogle.config
