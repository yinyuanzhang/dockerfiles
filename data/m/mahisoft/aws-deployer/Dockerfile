FROM alpine:3.8

RUN apk add --no-cache curl libc6-compat
RUN curl https://amazon-eks.s3-us-west-2.amazonaws.com/1.10.3/2018-07-26/bin/linux/amd64/aws-iam-authenticator -o /bin/aws-iam-authenticator -s && \
    chmod +x /bin/aws-iam-authenticator

RUN curl https://amazon-eks.s3-us-west-2.amazonaws.com/1.10.3/2018-07-26/bin/linux/amd64/kubectl -o /bin/kubectl -s && \
    chmod +x /bin/kubectl

RUN curl -L https://github.com/kubernetes/kompose/releases/download/v1.16.0/kompose-linux-amd64 -o /bin/kompose && \
    chmod +x /bin/kompose
