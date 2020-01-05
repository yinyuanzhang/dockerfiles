FROM atlassian/pipelines-awscli
RUN apk --update --no-cache add curl wget sudo

ENV KUBECTL_VERSION v1.17.0
RUN curl -LO "https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl"
RUN chmod +x ./kubectl
RUN sudo mv ./kubectl /usr/local/bin/kubectl

ENV KOPS_VERSION 1.15.0
RUN curl -LO "https://github.com/kubernetes/kops/releases/download/${KOPS_VERSION}/kops-linux-amd64"
RUN chmod +x kops-linux-amd64
RUN sudo mv kops-linux-amd64 /usr/local/bin/kops


