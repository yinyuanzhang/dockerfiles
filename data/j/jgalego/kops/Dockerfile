FROM ubuntu:trusty

LABEL Author João Galego <jgalego1990@gmail.com>

# Install Utilities
RUN apt-get update && apt-get install -y curl

# Install Kops
RUN curl -LO https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64 && \
    chmod +x kops-linux-amd64 && \
    mv kops-linux-amd64 /usr/local/bin/kops

ENTRYPOINT [ "kops" ]