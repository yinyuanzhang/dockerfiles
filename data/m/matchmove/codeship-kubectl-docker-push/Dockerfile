FROM ruby:2.3

RUN apt-get update && apt-get install -y curl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin/kubectl

COPY scripts/env_var_helper_client.sh scripts/env_var_helper_client.rb ./
RUN chmod +x env_var_helper_client.sh

ENTRYPOINT ["./env_var_helper_client.sh"]
