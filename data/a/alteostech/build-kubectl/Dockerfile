FROM bash:latest

RUN apk add --update curl git perl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.13.3/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && \
    mv ./kubectl /usr/local/bin/kubectl
    
RUN curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.12.7/2019-03-27/bin/linux/amd64/aws-iam-authenticator && \
    cp ./aws-iam-authenticator /usr/local/bin/aws-iam-authenticator && \
    chmod +x /usr/local/bin/aws-iam-authenticator
