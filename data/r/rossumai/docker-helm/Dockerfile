FROM alpine:3.7
RUN apk update && apk add --no-cache curl openssl python3 py3-click py3-yaml bash
RUN pip3 install boto3
RUN curl -s -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl
RUN mkdir -p ~/.kube
RUN curl -s https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get >get_helm.sh
RUN bash ./get_helm.sh
