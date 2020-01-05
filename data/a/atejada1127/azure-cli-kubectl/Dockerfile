FROM azuresdk/azure-cli-python:latest

LABEL authors="Albert Tejada <alberttejada@gmail.com>"

ENV KUBERNETES_VERSION=1.11.1
RUN wget https://storage.googleapis.com/kubernetes-release/release/v${KUBERNETES_VERSION}/bin/linux/amd64/kubectl -qO /usr/local/bin/kubectl
RUN chmod +x /usr/local/bin/kubectl
