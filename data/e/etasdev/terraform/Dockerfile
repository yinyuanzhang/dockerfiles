# build terraform k8s provider 
FROM golang:1.10 as builder
RUN go get github.com/sl1pm4t/terraform-provider-kubernetes &&\
    cd /go/src/github.com/sl1pm4t/terraform-provider-kubernetes &&\
    CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo .
 
# Build image based on terraform:light
# see https://github.com/hashicorp/docker-hub-images/blob/master/terraform/Dockerfile-light
FROM hashicorp/terraform:light

 #install bash
RUN apk add --no-cache bash

# intall terraform k8s provider 
COPY --from=builder /go/src/github.com/sl1pm4t/terraform-provider-kubernetes/terraform-provider-kubernetes /root/.terraform.d/plugins/

# install kubectl
# Note: Latest version may be found on:
# https://aur.archlinux.org/packages/kubectl-bin/
ADD https://storage.googleapis.com/kubernetes-release/release/v1.11.3/bin/linux/amd64/kubectl /usr/local/bin/kubectl

# install aws-iam-authenticator für k8s
ADD https://github.com/kubernetes-sigs/aws-iam-authenticator/releases/download/v0.3.0/heptio-authenticator-aws_0.3.0_linux_amd64 /usr/local/bin/aws-iam-authenticator

RUN chmod +x /usr/local/bin/*

ENTRYPOINT ["/bin/terraform"]
